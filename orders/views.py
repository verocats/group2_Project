
from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail, BadHeaderError

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        initial = {
            'first_name': request.user.get_full_name(),
            'email': request.user.email
        }
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            totalPrice = 0.00;
            order = form.save(commit=False)
            order.customerid = request.user.id
            order.totalprice = totalPrice
            order.email = request.user.email

            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                totalPrice += float(item['price']*item['quantity'])
            order.totalprice = totalPrice
            order.save()
            toaddresses= []
            toaddresses.append(request.user.email)
            send_mail('Order Placed Successfully', 'Hi '+order.last_name+'\n\nYour order of total $'+str(order.totalprice)+' has been successfully placed.\n\n Yours sincerely. \nEuropes Corner', request.user.email, toaddresses)

            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})

def order_list(request):
    orders = Order.objects.filter(customerid=request.user.id)
    return render(request,
                  'MyOrders.html',
                  {'orders': orders})

def order_detail(request, pk):
    orderItems = OrderItem.objects.filter(order=pk)
    return render(request,
                  'OrderDetail.html',
                  {'orderitems': orderItems})