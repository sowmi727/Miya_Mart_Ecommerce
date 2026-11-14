from django.shortcuts import render, redirect
from .models import Product, Order

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('home')


def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []

    for product in products:
        quantity = cart[str(product.id)]
        total = product.price * quantity

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total
        })

    grand_total = sum(item['total'] for item in cart_items)

    return render(request, 'store/cart.html', {
         'cart_items': cart_items,
         'grand_total': grand_total
})


   
   
 
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')

def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1

    request.session['cart'] = cart
    return redirect('cart')


def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]

    request.session['cart'] = cart
    return redirect('cart')

def checkout(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    grand_total = 0

    for product in products:
        quantity = cart[str(product.id)]
        total = product.price * quantity
        grand_total += total

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total
        })

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        Order.objects.create(
            customer_name=customer_name,
            phone=phone,
            address=address,
            total_amount=grand_total,
            payment_method=payment_method,
            payment_status='Pending'
  )

        request.session['cart'] = {}

        return redirect('order_success')

    return render(request, 'store/checkout.html', {
        'cart_items': cart_items,
        'grand_total': grand_total
    })

def order_success(request):
    order = Order.objects.order_by('-id').first()

    return render(request, 'store/order_success.html', {
        'order': order
    })