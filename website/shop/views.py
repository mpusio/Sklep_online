from django.shortcuts import render
from .models import Categories, Products, Orders
from .templates.shop import *
#sing up
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def category(request):
    categories = Categories.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'shop/category.html', context)

def details(request, id):
    categories = Categories.objects.get(id=id)
    products = Products.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'shop/details.html', context)

def insert(request, id, id2, id3):
    # username = request.POST.get['username']
    post = Categories.objects.get(id=id)

    product = Products.objects.get(id=id2)
    p = Orders(text=product.name, id_user_id=id3, id_product_id=product.id)
    p.save()
    context = {
        'product': product,
    }

    return render(request, 'shop/insert.html', context)

def delete(request):
    order = Orders.objects.all()
    context =  {
        'order': order,
    }
    return render(request, 'shop/delete.html', context)

def inf_delete(request, id):
    order = Orders.objects.get(id=id)
    order.delete()
    context = {
        'order': order,
    }
    return render(request, 'shop/inf_delete.html', context)

def update(request):
    product = Products.objects.all()
    context = {
        'product': product
    }
    return render(request, 'shop/update.html', context)

def inf_update(request, id):
    product = Products.objects.get(id=id)
    p = Products(id=id, price=str(int(product.price)-10), category_id=product.category_id, name=product.name)
    p.save()
    context = {
        'product': product
    }
    return render(request, 'shop/inf_update.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})

