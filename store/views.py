from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ReviewRating, ProductGallery, Variation, VariationManager
from carts.models import CartItem
from carts.views import _cart_id
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct
import json
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Avg, Count
from django.utils.text import slugify

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    
    # 카테고리 세션 초기화
    try:
        if request.session['category_name']:
            print (request.session['category_name'])
            del request.session['category_name']

    except:
        pass 
    
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by("-created_date")
        paginator = Paginator(products,9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

        
        my_dict=[]
        #
        id = []
        variation_category = []
        options_key_value = []
            
        for product in products.values('id'):
            id.append(product['id'])
        for i in id:    
            product_test = Product.objects.get(id=i)  
            variations = product_test.variation_set.all()
            for variation in variations:
                if variation.variation_category not in variation_category:
                    variation_category.append(variation.variation_category)
                
            # print(variation_category) variation_category 중복없이 뽑아옴
            

            for variation_key in variation_category:
                items = product_test.variation_set.filter(variation_category=variation_key)

                options_key_value.append(list(items.values('variation_category','variation_value')))


    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

        id = []
        variation_category = []
        options_key_value = []        
        
        for product in products.values('id'):
            id.append(product['id'])
        for i in id:    
            product_test = Product.objects.get(id=i)  
            variations = product_test.variation_set.all()
            for variation in variations:
                if variation.variation_category not in variation_category:
                    variation_category.append(variation.variation_category)
                
        # print(variation_category) # variation_category 중복없이 뽑아옴
            

            # for variation_key in variation_category:
            #     items = product_test.variation_set.filter(variation_category=variation_key)

            #     options_key_value.append(list(items.values('variation_category','variation_value')))

    # print(options_key_value)
    

    colors = set()
    sizes = set()
    
    for item in options_key_value:
        for variation in item:
            if variation['variation_category'] == 'color':
                colors.add(variation['variation_value'])
            elif variation['variation_category'] == 'size':
                sizes.add(variation['variation_value'])

    # print("Colors:", colors)
    # print("Sizes:", sizes)
    
    option_colors = sorted(list(colors))
    option_sizes = sorted(list(sizes))
    
    my_dict = {
        "colors":option_colors,
        "sizes":option_sizes
    }

    
    context = {
        'products': paged_products,
        'product_count': product_count,
        'my_dict':my_dict,
        # 'color':color,
        # 'size':size,


    }
    
    return render(request, 'store/store.html', context)

def update_results(request):
    global products
    global options_key_value

    if request.method == 'POST':
        
        sort_by_options = request.POST.get('sort_by')
        value_options = request.POST.getlist('key')
        previous_url = request.META.get('HTTP_REFERER', '')  # URL에 카테고리가 존재하는지 확인
        
        
        # print(f'sort_by_options : {sort_by_options}')
        # print(f'value_options : {value_options}')
                
        # 주소창에 카테고리 존재
        if 'category' in previous_url:
            print(1)
            # url 에서 슬러그 뽑아내기
            category_name_url = previous_url.split('/')
            category_name = category_name_url[-2]
            # session 초기화 및 새로 만들어서 카테고리 정보 담기
            request.session["category_name"] = category_name
            
            # 뽑아낸 slug 로 상품 필터링
            products = Product.objects.all().filter(is_available=True, category__slug = category_name)

            # 옵션을 선택했을때
            if len(value_options) > 0:
                products = products.filter(variation__variation_value__in = value_options)
                
                # 낮은 가격순
                lowToHigh = products.order_by('price')
                # 높은 가격순
                highToLow = products.order_by('-price')
                # 신상품순
                new = products.order_by('created_date')
                # 평균 별점순
                avg_review = products.annotate(avg_review=Avg('reviewrating__rating')).order_by('-avg_review')
                
                if sort_by_options == "lowToHigh":
                    products = lowToHigh
                elif sort_by_options == "highToLow":
                    products = highToLow
                elif sort_by_options == "new":
                    products = new
                else:
                    products = avg_review

            # 옵션을 선택하지 않았을 때 -> 동일 카테고리 + sort by로 정렬
            else:
                
                # 낮은 가격순
                lowToHigh = products.order_by('price')
                # 높은 가격순
                highToLow = products.order_by('-price')
                # 신상품순
                new = products.order_by('created_date')
                # 평균 별점순
                avg_review = products.annotate(avg_review=Avg('reviewrating__rating')).order_by('-avg_review')
                print('3')
                if sort_by_options == "lowToHigh":
                    products = lowToHigh
                elif sort_by_options == "highToLow":
                    products = highToLow
                elif sort_by_options == "new":
                    products = new
                else:
                    products = avg_review
            
            # 옵션 여부 불러와야함 
         
            my_dict=[]
            id = []
            variation_category = []
            options_key_value = []
                
            for product in products.values('id'):
                id.append(product['id'])
            for i in id:    
                product_test = Product.objects.get(id=i)  
                variations = product_test.variation_set.all()
                for variation in variations:
                    if variation.variation_category not in variation_category:
                        variation_category.append(variation.variation_category)
                    
                # print(variation_category) variation_category 중복없이 뽑아옴
                

                for variation_key in variation_category:
                    items = product_test.variation_set.filter(variation_category=variation_key)

                    options_key_value.append(list(items.values('variation_category','variation_value')))
        
        # 옵션 선택한 상태에서 한 번 더 선택할 때 -> 주소창은 test 옵션 존재할 때      
        elif 'update_results' in previous_url and len(value_options) != 0:
            print(2)

            # 이전에 만들어 놓았던 세션에서 카테고리 정보 갖고오기
            category_name = request.session.get("category_name")

            # 뽑아낸 카테고리 정보로 상품 필터링
            products = Product.objects.all().filter(is_available=True, category__slug = category_name)

            # 옵션을 선택했을때 (1개)
            if len(value_options) == 1:
                products = products.filter(variation__variation_value__in = value_options)
                
                # 낮은 가격순
                lowToHigh = products.order_by('price')
                # 높은 가격순
                highToLow = products.order_by('-price')
                # 신상품순
                new = products.order_by('created_date')
                # 평균 별점순
                avg_review = products.annotate(avg_review=Avg('reviewrating__rating')).order_by('-avg_review')
                
                if sort_by_options == "lowToHigh":
                    products = lowToHigh
                elif sort_by_options == "highToLow":
                    products = highToLow
                elif sort_by_options == "new":
                    products = new
                else:
                    products = avg_review

            # 옵션을 선택했을때 (2개 이상)
            elif len(value_options) > 1:
                print("중복검사")
                for value in value_options:
                    
                    products = products.filter(variation__variation_value = value)
                    print(products)
                
                # 낮은 가격순
                lowToHigh = products.order_by('price')
                # 높은 가격순
                highToLow = products.order_by('-price')
                # 신상품순
                new = products.order_by('created_date')
                # 평균 별점순
                avg_review = products.annotate(avg_review=Avg('reviewrating__rating')).order_by('-avg_review')
                
                if sort_by_options == "lowToHigh":
                    products = lowToHigh
                elif sort_by_options == "highToLow":
                    products = highToLow
                elif sort_by_options == "new":
                    products = new
                else:
                    products = avg_review

            # 옵션을 선택하지 않았을 때 -> 동일 카테고리 + sort by로 정렬
            else:
                
                # 낮은 가격순
                lowToHigh = products.order_by('price')
                # 높은 가격순
                highToLow = products.order_by('-price')
                # 신상품순
                new = products.order_by('created_date')
                # 평균 별점순
                avg_review = products.annotate(avg_review=Avg('reviewrating__rating')).order_by('-avg_review')
                
                if sort_by_options == "lowToHigh":
                    products = lowToHigh
                elif sort_by_options == "highToLow":
                    products = highToLow
                elif sort_by_options == "new":
                    products = new
                else:
                    products = avg_review
            
            # 옵션 여부 불러와야함 
         
            my_dict=[]
            id = []
            variation_category = []
            options_key_value = []
                
            for product in products.values('id'):
                id.append(product['id'])
            for i in id:    
                product_test = Product.objects.get(id=i)  
                variations = product_test.variation_set.all()
                for variation in variations:
                    if variation.variation_category not in variation_category:
                        variation_category.append(variation.variation_category)
                    
                # print(variation_category) variation_category 중복없이 뽑아옴
                

                for variation_key in variation_category:
                    items = product_test.variation_set.filter(variation_category=variation_key)

                    options_key_value.append(list(items.values('variation_category','variation_value')))

        # 카테고리 옵션은 존재하지 않지만 url 은 여전히 test 일 때
        elif 'update_results' in previous_url and len(value_options) == 0 and request.session.has_key('category_name'):
            print(3)
            
        # 기존 카테고리 목록 유지해야되는 경우
        
            # 이전에 만들어 놓았던 세션에서 카테고리 정보 갖고오기
            category_name = request.session.get("category_name")
            # 뽑아낸 카테고리 정보로 상품 필터링
            products = Product.objects.all().filter(is_available=True, category__slug = category_name)

            # 낮은 가격순
            lowToHigh = products.order_by('price')
            # 높은 가격순
            highToLow = products.order_by('-price')
            # 신상품순
            new = products.order_by('created_date')
            # 평균 별점순
            avg_review = products.annotate(avg_review=Avg('reviewrating__rating')).order_by('-avg_review')
            
            if sort_by_options == "lowToHigh":
                products = lowToHigh
            elif sort_by_options == "highToLow":
                products = highToLow
            elif sort_by_options == "new":
                products = new
            else:
                products = avg_review
         
            id = []
            variation_category = []
            options_key_value = []        
            
            for product in products.values('id'):
                id.append(product['id'])
            for i in id:    
                product_test = Product.objects.get(id=i)  
                variations = product_test.variation_set.all()
                for variation in variations:
                    if variation.variation_category not in variation_category:
                        variation_category.append(variation.variation_category)
                    

                for variation_key in variation_category:
                    items = product_test.variation_set.filter(variation_category=variation_key)

                    options_key_value.append(list(items.values('variation_category','variation_value')))
            
        # 카테고리가 없으면
        else:
            print(4)
            
            products = Product.objects.all().filter(is_available=True)
            
            # 낮은 가격순
            lowToHigh = products.order_by('price')
            # 높은 가격순
            highToLow = products.order_by('-price')
            # 신상품순
            new = products.order_by('created_date')
            # 평균 별점순
            avg_review = Product.objects.annotate(avg_review=Avg('reviewrating__rating')).order_by('-avg_review')
            
            if sort_by_options == "lowToHigh":
                products = lowToHigh
            elif sort_by_options == "highToLow":
                products = highToLow
            elif sort_by_options == "new":
                products = new
            else:
                products = avg_review
         
            id = []
            variation_category = []
            options_key_value = []        
            
            for product in products.values('id'):
                id.append(product['id'])
            for i in id:    
                product_test = Product.objects.get(id=i)  
                variations = product_test.variation_set.all()
                for variation in variations:
                    if variation.variation_category not in variation_category:
                        variation_category.append(variation.variation_category)
                
                
    paginator = Paginator(products,9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()

    colors = set()
    sizes = set()
    
    for item in options_key_value:
        for variation in item:
            if variation['variation_category'] == 'color':
                colors.add(variation['variation_value'])
            elif variation['variation_category'] == 'size':
                sizes.add(variation['variation_value'])

    # print("Colors:", colors)
    # print("Sizes:", sizes)
    
    option_colors = sorted(list(colors))
    option_sizes = sorted(list(sizes))
    
    my_dict = {
        "colors":option_colors,
        "sizes":option_sizes
    }

    
    context = {
        'products': paged_products,
        'product_count': product_count,
        'my_dict':my_dict,


    }
    
    
    return render(request, 'store/filtered_store.html', context)
    
 
        
            

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None

    # Get the reviews
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    # Get the product gallery
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

    context = {
        'single_product': single_product,
        'in_cart'       : in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'product_gallery': product_gallery,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)

