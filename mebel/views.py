from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm
from .models import Categories, Products, Portfolio, Team, Review
from django.core.mail import send_mail
import telebot
from .forms import SubscribeForm
from .models import Products
from django.views import View
from blog.models import Post
from django.views.generic import DetailView

bot = telebot.TeleBot("1355993371:AAGdwvhPEIIzb2vFV8Rtw4d5v-0SneeZBs4")


def footer(request):
    form = SubscribeForm()
    context = {
        'form':form
    }
    return render(request, 'footer.html', context)

def index(request):
    posts = Post.objects.all().order_by('-date')[:3]
    product = Products.objects.filter(popularity__exact=True)

    paginator = Paginator(product, 6)
    products = paginator.get_page(1)

    context = {
        'posts': posts,
        'products': products
    }
    return render(request, 'meb/index.html', context)


def shop(request, slug_category=None):
    category = Categories.objects.all()
    product = Products.objects.all().order_by('-id')

    price_from = request.GET.get("min", "")
    price_to = request.GET.get("max", "")
    sorting = request.GET.get("sort", "")

    if sorting == '':
        sorting = '-name'

    if price_from == '':
        price_from = '0'
        price_to = '500000'

    product = Products.objects.order_by(sorting).filter(price__gte=int(price_from), price__lte=int(price_to))

    selected_category = ''

    if slug_category:
        category = Categories.objects.all()
        selected_category = get_object_or_404(Categories, slug_category=slug_category)
        product = Products.objects.filter(category=selected_category).order_by('-id')

        price_from = request.GET.get("min", "")
        price_to = request.GET.get("max", "")

        if price_from == '':
            price_from = '0'
            price_to = '500000'
        else:
            product = Products.objects.filter(category=selected_category, price__gte=int(price_from),
                                              price__lte=int(price_to)).order_by('-id')

    paginator = Paginator(product, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cart_product_form = CartAddProductForm()

    context = {
        'price_from': price_from,
        'price_to': price_to,
        'category': category,
        'product': product,
        'page_obj': page_obj,
        'selected_category': selected_category,
        'cart_product_form': cart_product_form,
    }

    return render(request, 'meb/shop.html', context)


def about(request):
    teams = Team.objects.all()
    reviews = Review.objects.all()
    posts = Post.objects.all().order_by('-date')[:3]
    context = {
        'teams': teams,
        'reviews': reviews,
        'posts': posts,
    }
    return render(request, 'meb/about.html', context)


def contact(request):
    return render(request, 'meb/contact.html')


def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'meb/portfolio.html', context)


class SubscribeView(View):
    def post(self, request):
        # if request.method == 'POST':
        form = SubscribeForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data['mail']
            subject = 'Новая заявка на подписку!'
            from_email = 'no-reply@bindoors.ru'
            to_email = ['aitofullstackdev@gmail.com', 'aitolivelive@gmail.com']
            message = 'Новая заявка на подписку!' + '\r\n' + '\r\n' + 'Почта: ' + mail

            send_mail(subject, message, from_email, to_email, fail_silently=False)
            bot.send_message(-1001450383553, message)
        return redirect('home')


def thank_you(request):
    return render(request, 'meb/thank-you.html')


def wrong(request):
    return render(request, 'meb/wrong.html')


def design(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/ideas.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/article.html'