import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from .models import Product

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'website' : 'Website toko bola',
        'name': 'Website ini milik Muhammad Geriya Itsa dengan NPM 2406434172',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        messages.success(request, "Produk berhasil dibuat!")
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize('xml', product_list)
    return HttpResponse(xml_data, content_type='application/xml')

def show_xml_by_id(request, product_id):
    try: 
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': product.id,
            'name': product.name,
            'category': product.category,
            # Try to provide a usable thumbnail URL/string
            'thumbnail': (product.thumbnail.url if hasattr(product.thumbnail, 'url') else str(product.thumbnail)) if product.thumbnail else "",
            'price': product.price,
            'description': product.description,
            'is_featured': product.is_featured,
            'user': product.user.username if product.user else None,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'thumbnail': product.thumbnail if product.thumbnail else None,
            'price': product.price,
            'description': product.description,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id and product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Selamat datang, {user.username}!")
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, "Anda telah logout. Selamat datang kembali :) ")
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.info(request, "Produk berhasil diperbarui!")
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    messages.error(request, "Produk telah dihapus!")
    return HttpResponseRedirect(reverse('main:show_main'))

def beranda(request):
    context = {
        "title": "Beranda",
        "description": "Selamat datang di Football Product! Website ini menyediakan produk perlengkapan sepak bola terbaik.",
        "features": [
            "Cek produk terbaru",
            "Buat dan kelola produk sendiri",
        ]
    }
    return render(request, "beranda.html", context)

# ...existing code...

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'Authentication required'}, status=403)

    name = strip_tags(request.POST.get("name", "")).strip()
    description = strip_tags(request.POST.get("description", "")).strip()
    category = strip_tags(request.POST.get("category", "")).strip()
    thumbnail = strip_tags(request.POST.get("thumbnail", "")).strip() or None
    is_featured = request.POST.get("is_featured") == 'on'
    price_raw = strip_tags(request.POST.get("price", "")).strip()

    errors = {}
    if not name:
        errors['name'] = 'Nama produk wajib diisi.'
    if not category:
        errors['category'] = 'Kategori wajib dipilih.'
    if price_raw == '':
        errors['price'] = 'Harga wajib diisi.'
    else:
        try:
            price = int(price_raw)
            if price < 0:
                errors['price'] = 'Harga tidak boleh negatif.'
        except ValueError:
            errors['price'] = 'Harga harus berupa angka integer.'

    if errors:
        return JsonResponse({'errors': errors}, status=400)

    product = Product(
        name=name,
        description=description,
        category=category,
        thumbnail=thumbnail,
        price=price,
        is_featured=is_featured,
        user=request.user
    )
    product.save()

    return JsonResponse({'id': product.id, 'detail': 'created'}, status=201)
