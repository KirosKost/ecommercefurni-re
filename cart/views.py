import telebot
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.http import require_POST
from mebel.models import Products
from .cart import Cart
from .forms import CartAddProductForm, OrderSendForm

bot = telebot.TeleBot("1355993371:AAGdwvhPEIIzb2vFV8Rtw4d5v-0SneeZBs4")


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if cd['colors'] == '':
            cd['colors'] = 'Не задан'
        if cd['sizes'] == '':
            cd['sizes'] = 'Не задан'
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'], colors=cd['colors'],
                 sizes=cd['sizes'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'cart/cart.html', context)


def order(request):
    return render(request, 'cart/order.html')


class OrderSendView(View):
    def post(self, request):
        if request.method == 'POST':
            form = OrderSendForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                if form.cleaned_data['mail'] == '':
                    mail = 'Не указана'
                else:
                    mail = form.cleaned_data['mail']
                cart = Cart(request)
                message = 'Поступил новый заказ!\r\n\r\nИмя: ' + name + '\r\nТелефон: ' + phone + '\r\nПочта: ' \
                          + mail + '\r\n\r\nПродукты\r\n\r\n'

                for c in cart:
                    message += 'Название: ' + str(c['product']) + '\r\n'
                    message += 'Цвет: ' + c['colors'] + '\r\n'
                    message += 'Размер: ' + c['sizes'] + '\r\n'
                    message += 'Цена: ' + str(c['price']) + '\r\n\r\n'

                message += 'Общая стоимость: ' + str(cart.get_total_price())

                bot.send_message(628980737, message)
                Cart.clear(cart)
                return redirect('thank-you')
            return redirect('wrong')
