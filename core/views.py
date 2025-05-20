from django.shortcuts import render, get_object_or_404
from products.models import LEDProduct, StageProduct, SoundProduct, LightingProduct, AccessoryProduct

def home(request):
    return render(request, 'index.html')

def category_products(request, category):
    # Map URL slugs to model classes and display names
    category_map = {
        'led': (LEDProduct, 'LED Displays'),
        'stage': (StageProduct, 'Stage Equipment'),
        'sound': (SoundProduct, 'Sound Equipment'),
        'lighting': (LightingProduct, 'Lighting Equipment'),
        'accessories': (AccessoryProduct, 'Accessories')
    }
    
    # Get the model class and display name for the requested category
    model_class, display_name = category_map.get(category, (None, None))
    
    if model_class is None:
        # Handle invalid category
        return render(request, 'products/category.html', {
            'products': [],
            'category': 'Category Not Found'
        })
    
    # Get available products for the category
    products = model_class.objects.filter(available=True)
    
    return render(request, 'products/category.html', {
        'products': products,
        'category': display_name,
        'category_slug': category  # Add this line to pass the slug
    })

def product_detail(request, category, product_id):
    # Map URL slugs to model classes and display names
    category_map = {
        'led': LEDProduct,
        'stage': StageProduct,
        'sound': SoundProduct,
        'lighting': LightingProduct,
        'accessories': AccessoryProduct
    }
    
    # Get the model class for the requested category
    model_class = category_map.get(category)
    
    if model_class is None:
        # Handle invalid category
        return render(request, 'product-detail.html', {
            'product': None,
            'error': 'Category Not Found'
        })
    
    # Get the product
    product = get_object_or_404(model_class, id=product_id, available=True)
    
    return render(request, 'products/product-detail.html', {
        'product': product,
        'category': category
    })

