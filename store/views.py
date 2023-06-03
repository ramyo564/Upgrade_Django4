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

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by("-created_date")
        paginator = Paginator(products,9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        #
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
            

            for variation_key in variation_category:
                items = product_test.variation_set.filter(variation_category=variation_key)

                options_key_value.append(list(items.values('variation_category','variation_value')))

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
