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
    
    return render(request, 'store/test.html', context)

def test(request, category_slug=None):
    if request.method == 'POST':
        sort_by_options = request.POST.get('sort_by')
        value_options = request.POST.getlist('key')
        previous_url = request.META.get('HTTP_REFERER', '')  # URL에 카테고리가 존재하는지 확인
        
        
        # print(f'sort_by_options : {sort_by_options}')
        # print(f'value_options : {value_options}')
                
        # 주소창에 카테고리 존재
        if 'category' in previous_url:

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
        elif 'test' in previous_url and len(value_options) != 0:
 

            # 이전에 만들어 놓았던 세션에서 카테고리 정보 갖고오기
            category_name = request.session.get("category_name")

            # 뽑아낸 카테고리 정보로 상품 필터링
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
        elif 'test' in previous_url and len(value_options) == 0 and request.session.has_key('category_name'):

            
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
        
       
        
        return render(request, 'store/test.html', context)
            


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

def update_results(request):
    if request.method == 'POST':
        selected_values = json.loads(request.POST.get('selectedValues'))
        selected_sort_option = request.POST.get('selectedSortOption')
        previous_url = request.META.get('HTTP_REFERER', '')  # 이전 URL 가져오기
        
        # JSON 쓸 데 없는 문자 지우기
        fix_selected_values = []
        for i in range(0, len(selected_values)):
            x = selected_values[i].strip('\n').lstrip().rstrip()
            fix_selected_values.append(x)
            
        print(f"selected_values 옵션 선택한거 {fix_selected_values}")
        print(f"selected_sort_option 정렬방법 {selected_sort_option}")
        
        # 이전에 선택한 옵션과 새로 선택한 옵션, 그리고 카테고리 모두 존재하는 상품 필터링
        matching_products = Product.objects.filter(variation__variation_value__in=fix_selected_values).order_by("-created_date").distinct()
        
        for value in fix_selected_values:
            matching_products = matching_products.filter(variation__variation_value=value)
        
        # 이전에 선택한 카테고리와 새로 선택한 카테고리 모두에 대한 필터링
        previous_categories = set(matching_products.values_list('category__category_name', flat=True))
        new_categories = set(Product.objects.filter(variation__variation_value__in=fix_selected_values).values_list('category__category_name', flat=True))
        
        common_categories = previous_categories.intersection(new_categories)
        
        matching_products = matching_products.filter(category__category_name__in=common_categories)
        
        # 확인을 위해 카테고리 출력
        for product in matching_products:
            print(f"Product {product.id}: Category '{product.category.category_name}'")
        
        paginator = Paginator(matching_products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = matching_products.count()
        
        id = []
        variation_category = []
        options_key_value = []
        
        for product in matching_products.values('id'):
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
            
        colors = set()
        sizes = set()
        
        for item in options_key_value:
            for variation in item:
                if variation['variation_category'] == 'color':
                    colors.add(variation['variation_value'])
                elif variation['variation_category'] == 'size':
                    sizes.add(variation['variation_value'])
        
        option_colors = sorted(list(colors))
        option_sizes = sorted(list(sizes))
        
        my_dict = {
            "colors": option_colors,
            "sizes": option_sizes
        }
        
        context = {
            'products': paged_products,
            'product_count': product_count,
            'my_dict': my_dict,
        }
    
    else:
        print('error')
        
    return render(request, 'store/filtered_store.html', context=context)


def second_update_results(request):
    if request.method == 'POST':
        # POST 요청 처리 및 필요한 작업 수행
        # ...

        # 응답 데이터 반환
        response_data = {
            'message': 'Update successful'
        }
        return JsonResponse(response_data)


    if request.method == 'POST':
        selected_values = json.loads(request.POST.get('selectedValues'))
        selected_sort_option = request.POST.get('selectedSortOption')
        previous_url = request.META.get('HTTP_REFERER', '')  # 이전 URL 가져오기

        # JSON 쓸 데 없는 문자 지우기
        fix_selected_values = []
        for i in range(0, len(selected_values)):
            x = selected_values[i].strip('\n').lstrip().rstrip()
            fix_selected_values.append(x)
            
        print(f"selected_values 옵션 선택한거 {fix_selected_values}")
        print(f"selected_sort_option 정렬방법 {selected_sort_option}")
        
        # 매치된 상품들의 카테고리가 일치할 경우
        
        
        
        # 이전에 선택한 옵션과 새로 선택한 옵션 모두 존재하는 상품 필터링
        matching_products = Product.objects.filter(variation__variation_value__in=fix_selected_values).order_by("-created_date").distinct()
        for value in fix_selected_values:
            matching_products = matching_products.filter(variation__variation_value=value)
            
        # 매칭된 상품들이 카테고리가 일치하는지 확인 
        
         
        
        
        
        ###
        
        paginator = Paginator(matching_products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = matching_products.count()
        
        id = []
        variation_category = []
        options_key_value = []
        
        for product in matching_products.values('id'):
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
            
        colors = set()
        sizes = set()
        
        for item in options_key_value:
            for variation in item:
                if variation['variation_category'] == 'color':
                    colors.add(variation['variation_value'])
                elif variation['variation_category'] == 'size':
                    sizes.add(variation['variation_value'])

        option_colors = sorted(list(colors))
        option_sizes = sorted(list(sizes))
        
        my_dict = {
            "colors": option_colors,
            "sizes": option_sizes
        }
        
        context = {
            'products': paged_products,
            'product_count': product_count,
            'my_dict': my_dict,
        }
    else:
        print('error')
        
    return render(request, 'store/filtered_store.html', context=context)


def update_results_real(request):
    if request.method == 'POST':
        selected_values = json.loads(request.POST.get('selectedValues'))
        selected_sort_option = request.POST.get('selectedSortOption')
        previous_url = request.META.get('HTTP_REFERER', '')  # 이전 URL 가져오기
        
        # JSON 쓸 데 없는 문자 지우기
        fix_selected_values = []
        for i in range(0, len(selected_values)):
            x = selected_values[i].strip('\n').lstrip().rstrip()
            fix_selected_values.append(x)
            
        print(f"selected_values 옵션 선택한거 {fix_selected_values}")
        print(f"selected_sort_option 정렬방법 {selected_sort_option}")
        
        # 선택한 옵션이 존재하는지 매칭하기
        filtered_pk_list = []
        matching_products = Product.objects.filter(variation__variation_value__in=fix_selected_values).order_by("-created_date").distinct()
        matching_products_pks  = matching_products.values_list('pk', flat=True)
        
        # 매칭된 상품 pk 추출
        for i in matching_products_pks:
            filtered_pk_list.append(i)
       
        paginator = Paginator(matching_products,9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = matching_products.count()
        
        
        id = []
        variation_category = []
        options_key_value = []        
    
        for product in matching_products.values('id'):
            id.append(product['id'])
            
        for i in id:    
            product_test = Product.objects.get(id=i)  
            variations = product_test.variation_set.all()
            for variation in variations:
                if variation.variation_category not in variation_category:
                    variation_category.append(variation.variation_category)
                
        # print(variation_category) # variation_category 중복없이 뽑아옴
            

            for variation_key in variation_category:
                items = product_test.variation_set.filter(variation_category=variation_key)

                options_key_value.append(list(items.values('variation_category','variation_value')))            
            

        # # 갱신된 값이 있을 때 끝
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
    
    
    else:
        print('error')
        
    return render(request, 'store/filtered_store.html', context=context)


def update_results_1(request):

    if request.method == 'POST':
        

        selected_values = json.loads(request.POST.get('selectedValues'))
        selected_sort_option = request.POST.get('selectedSortOption')
        previous_url = request.META.get('HTTP_REFERER', '')  # 이전 URL 가져오기

    
        
        # JSON 쓸 데 없는 문자 지우기
        fix_selected_values = []
        for i in range(0, len(selected_values)):
            x = selected_values[i].strip('\n').lstrip().rstrip()
            fix_selected_values.append(x)
            
        print(f"selected_values 옵션 선택한거 {fix_selected_values}")
        print(f"selected_sort_option 정렬방법 {selected_sort_option}")
        
        # 선택한 옵션이 존재하는지 매칭하기
        matching_products = Product.objects.filter(variation__variation_value__in=fix_selected_values).order_by("-created_date").distinct()


        # # 중복 필터링
        # if len(saved_pks) != 0:
        #     print(1)
        #     filtered_pk_list = []
        #     # 이미 선택된 아이템 내에서 필터링
            
        #     # 선택한 옵션만 있는 아이템 필터링
        #     matching_products = Product.objects.filter(pk__in=saved_pks).order_by("-created_date").distinct()
        #     matching_products = Product.objects.filter(Q(pk__in=saved_pks) | Q(variation__variation_value__in=fix_selected_values)).order_by("-created_date").distinct()
        #     matching_products_pks  = matching_products.values_list('pk', flat=True)
        #     for i in matching_products_pks:
        #         filtered_pk_list.append(i)
   
        #     request.session['filtered_pk_list'] = filtered_pk_list
            
        #     paginator = Paginator(matching_products,9)
        #     page = request.GET.get('page')
        #     paged_products = paginator.get_page(page)
        #     product_count = matching_products.count()

        #     id = []
        #     variation_category = []
        #     options_key_value = []        
        
        #     for product in matching_products.values('id'):
        #         id.append(product['id'])
        #     #     #초기화
        #     # request.session['filtered_pk_list'] = []

        # # 밑에부터 쓰잘데기 없음 일단 보류
        # elif 'category' in previous_url:
            
        #     if len(request.session.get('category_pk_list',[])) == 0 and len(request.session.get('category_session_used',[])) == 0:
        #         print("카테고리에서 완전 처음일 때")
        #         category_pk_list = []
        #         matching_products = Product.objects.filter(variation__variation_value__in=fix_selected_values).order_by("-created_date").distinct()
        #         matching_products_pks  = matching_products.values_list('pk', flat=True)
        #         for i in matching_products_pks:
        #             category_pk_list.append(i)

        #         request.session['category_pk_list'] = category_pk_list    
        #         print(f'category_pk_list : {category_pk_list}')
        #         paginator = Paginator(matching_products,9)
        #         page = request.GET.get('page')
        #         paged_products = paginator.get_page(page)
        #         product_count = matching_products.count()

        #         id = []
        #         variation_category = []
        #         options_key_value = []        

        #         for product in matching_products.values('id'):
        #             id.append(product['id'])
                    
        #     elif len(request.session.get('category_pk_list',[])) != 0 and len(request.session.get('catefory_session_used',[])) != 0:
        #         print("카테고리 클릭 처음 X 그리고 pk 리스트가 남아 있을 때")
                
        #         category_pk_list = request.session.get('category_pk_list',[])
        #         matching_products = Product.objects.filter(pk__in=category_pk_list).order_by("-created_date").distinct()
        #         print(f'matching_products : {matching_products}')
        #         print(f'category_pk_list : {category_pk_list}')
        #         print(f'fix_selected_values : {fix_selected_values}')
        #         matching_products_pks  = matching_products.values_list('pk', flat=True)
        #         for i in matching_products_pks:
        #             category_pk_list.append(i)

        #         request.session['category_pk_list'] = []    
        #         request.session['category_session_used'] = ["yes"] 
        #         paginator = Paginator(matching_products,9)
        #         page = request.GET.get('page')
        #         paged_products = paginator.get_page(page)
        #         product_count = matching_products.count()

        #         id = []
        #         variation_category = []
        #         options_key_value = []        

        #         for product in matching_products.values('id'):
        #             id.append(product['id'])

            
        #     else:
        #         print("카테고리에서 추가 옵션 선택")
        #         print("카테고리는 사용 했는데 pk 리스트는 안남아 있을 때")

        #         # 1개만 선택 했을 때
        #         x = len(request.session.get('category_session_used',[]))
        #         y = len(request.session.get('category_pk_list',[]))
        #         print (f"x = {x} y = {y}")
        #         # 2개 이상 선택 했을 때
                
        #         category_pk_list = request.session.get('category_pk_list',[])
        #         matching_products = Product.objects.filter(variation__variation_value__in=fix_selected_values).order_by("-created_date").distinct()
        #         print(f'matching_products : {matching_products}')
        #         print(f'category_pk_list : {category_pk_list}')
        #         print(f'fix_selected_values : {fix_selected_values}')
        #         matching_products_pks  = matching_products.values_list('pk', flat=True)
        #         for i in matching_products_pks:
        #             category_pk_list.append(i)

        #         request.session['category_pk_list'] = []    
        #         request.session['category_session_used'] = ["yes"] 
        #         paginator = Paginator(matching_products,9)
        #         page = request.GET.get('page')
        #         paged_products = paginator.get_page(page)
        #         product_count = matching_products.count()

        #         id = []
        #         variation_category = []
        #         options_key_value = []        

        #         for product in matching_products.values('id'):
        #             id.append(product['id'])
                
        # else:
        #     # 옵션에 맞는 아이템 필터링
        #     print(3)
        #     filtered_pk_list = []
        #     matching_products = Product.objects.filter(variation__variation_value__in=fix_selected_values).order_by("-created_date").distinct()
        #     matching_products_pks  = matching_products.values_list('pk', flat=True)
        #     for i in matching_products_pks:
        #         filtered_pk_list.append(i)

        #     request.session['filtered_pk_list'] = filtered_pk_list     
        #     paginator = Paginator(matching_products,9)
        #     page = request.GET.get('page')
        #     paged_products = paginator.get_page(page)
        #     product_count = matching_products.count()

        #     id = []
        #     variation_category = []
        #     options_key_value = []        

        #     for product in matching_products.values('id'):
        #         id.append(product['id'])
                
                
                
    #     for i in id:    
    #         product_test = Product.objects.get(id=i)  
    #         variations = product_test.variation_set.all()
    #         for variation in variations:
    #             if variation.variation_category not in variation_category:
    #                 variation_category.append(variation.variation_category)
                
    #     # print(variation_category) # variation_category 중복없이 뽑아옴
            

    #         for variation_key in variation_category:
    #             items = product_test.variation_set.filter(variation_category=variation_key)

    #             options_key_value.append(list(items.values('variation_category','variation_value')))



    #     # # 갱신된 값이 있을 때 끝
    #     colors = set()
    #     sizes = set()
        
    #     for item in options_key_value:
    #         for variation in item:
    #             if variation['variation_category'] == 'color':
    #                 colors.add(variation['variation_value'])
    #             elif variation['variation_category'] == 'size':
    #                 sizes.add(variation['variation_value'])

    #     # print("Colors:", colors)
    #     # print("Sizes:", sizes)
        
    #     option_colors = sorted(list(colors))
    #     option_sizes = sorted(list(sizes))
        
    #     my_dict = {
    #         "colors":option_colors,
    #         "sizes":option_sizes
    #     }

        
    #     context = {
    #         'products': paged_products,
    #         'product_count': product_count,
    #         'my_dict':my_dict,
    #     }
    
    
    # else:
    #     print('error')
        
    # return render(request, 'store/filtered_store.html', context=context)
