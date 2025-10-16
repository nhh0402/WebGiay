from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def product_detail(request, product_id):
    # sau này bạn có thể lấy sản phẩm từ DB theo id
    return render(request, 'product-detail.html', {'product_id': product_id})

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def order_complete(request):
    return render(request, 'order-complete.html')

def contact(request):
    return render(request, 'contact.html')

def men(request):
    return render(request, 'men.html')

def women(request):
    return render(request, 'women.html')
def about(request):
    return render(request, 'about.html')

