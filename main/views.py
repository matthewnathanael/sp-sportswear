from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
import requests

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  
    category_filter = request.GET.get("category")
    if filter_type == "all":
        product_list = Product.objects.all()
    elif filter_type == "featured":
        product_list = Product.objects.filter(is_featured=True)
    else:
        product_list = Product.objects.filter(user=request.user)
    
        
    context = {
        'name': request.user.username,
        'class': 'PBP E',
        'nama_aplikasi': 'SP Sportswear',
        'product_list': product_list,   
        'last_login': request.COOKIES.get('last_login', 'Never'),  
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_product.html", context)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def delete_product_ajax(request, id): # <-- FUNGSI DELETE BARU
    try:
        # Ensure user owns the product (security check)
        product = Product.objects.get(pk=id, user=request.user) 
        product.delete()
        return HttpResponse("DELETED", status=200)
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found or access denied")


# @csrf_exempt
# @require_POST
# @login_required(login_url='/login')
# def add_product_entry_ajax(request):
   
#     form = ProductForm(request.POST)
    
#     if form.is_valid():
#         new_product = form.save(commit = False)
#         new_product.user = request.user # Menggunakan request.user karena @login_required
        
#         # FIX: Explicitly handle the is_featured checkbox
#         # If the checkbox is unchecked, it won't be in request.POST, and we need to ensure it's False.
#         # This prevents a potential unhandled exception when saving the ModelForm instance.
#         new_product.is_featured = request.POST.get("is_featured") == 'on'
        
#         new_product.save() # Saves the product with the correct is_featured value
  
#         return JsonResponse({"status": "CREATED", "message": "Produk berhasil ditambahkan!"}, status=201)
    
#     errors = dict(form.errors.items())
#     return JsonResponse({"status": "ERROR", "message": "Gagal menambahkan produk. Periksa input Anda.", "errors": errors}, status=400)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def add_product_entry_ajax(request):
    try:
        # 1. Mengambil data dari request.POST
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        thumbnail = request.POST.get("thumbnail")
        category = request.POST.get("category")
        stock = request.POST.get("stock")
        rating_str = request.POST.get("rating")
        brand = request.POST.get("brand")
        
        # 2. Penanganan checkbox dan user
        is_featured = request.POST.get("is_featured") == 'on' 
        user = request.user
        
        # 3. Validasi dan Konversi Data
        
        # Validasi sederhana untuk field yang harus ada dan numerik
        if not all([name, price, description, category, stock]):
            return JsonResponse({"status": "ERROR", "message": "Missing required fields."}, status=400)
        
        # Konversi ke tipe data yang benar dan membersihkan tag HTML (strip_tags)
        price = int(price)
        stock = int(stock)
        rating = float(rating_str) if rating_str else None # Float field
        
        name = strip_tags(name)
        description = strip_tags(description)
        brand = strip_tags(brand) if brand else ""
        
        # 4. Membuat instance Product baru
        new_product = Product(
            name=name, 
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
            stock=stock,
            rating=rating,
            brand=brand,
            user=user # Set user dari request
        )
        new_product.save()
        
        # 5. Menggunakan JsonResponse agar kompatibel dengan JS di modal.html
        return JsonResponse({"status": "CREATED", "message": "Produk berhasil ditambahkan (Manual)."}, status=201)

    except (ValueError, TypeError) as e:
        # Error saat konversi tipe data (misal: price bukan angka)
        return JsonResponse({"status": "ERROR", "message": f"Invalid input data: {e}"}, status=400)
    except Exception as e:
        # Catch-all untuk error lain (misal: IntegrityError)
        return JsonResponse({"status": "ERROR", "message": f"An unexpected error occurred: {e}"}, status=500)

def edit_product_entry_ajax(request, id): # <--- Tambahkan parameter id
    
    
    product_id = id # Gunakan ID dari URL path

    try:
        # Gunakan product_id (dari URL) untuk mencari instance
        product_instance = Product.objects.get(pk=product_id, user=request.user)
    except Product.DoesNotExist:
        return JsonResponse({"status": "ERROR", "message": "Produk tidak ditemukan atau akses ditolak."}, status=404) #

    # Kirimkan data POST, tapi Django akan mengabaikan field 'id' jika ada di POST body 
    # karena kita sudah menyediakan instance-nya.
    form = ProductForm(request.POST, instance=product_instance) #

    if form.is_valid(): #
        updated_product = form.save(commit=False) #
        updated_product.is_featured = request.POST.get("is_featured") == 'on'
        updated_product.save() #
        return JsonResponse({"status": "UPDATED", "message": "Produk berhasil diperbarui."}, status=200) #

    # Jika tidak valid, kembalikan error JSON
    errors = dict(form.errors.items()) #
    return JsonResponse({"status": "ERROR", "message": "Gagal memperbarui produk. Periksa input Anda.", "errors": errors}, status=400) #


@login_required(login_url='/login')
def show_products(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)



def edit_product(request, id):
    products = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=products)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))



def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "my":
        # Ambil produk milik user yang sedang login
        product_list = Product.objects.select_related('user').filter(user=request.user)
    else: 
        # Ambil semua produk
        product_list = Product.objects.select_related('user').all()
    data = [
        {
           'id': str(product.id),
            'name': product.name, # Mengganti 'title' dengan 'name'
            'price': product.price,
            'description': product.description, # Mengganti 'content' dengan 'description'
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'rating': product.rating,
            'brand': product.brand,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
         return HttpResponse(status=404)
     
def show_json_by_id(request, product_id):
    try:
        # Menggunakan select_related untuk mengambil data User
        product = Product.objects.select_related('user').get(pk=product_id)
        
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'rating': product.rating,
            'brand': product.brand,
            'user_id': product.user_id,
            # Menambahkan username penjual (Seller)
            'user_username': product.user.username if product.user_id and product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Product not found'}, status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

# def logout_user(request):
#     logout(request)
#     response = HttpResponseRedirect(reverse('main:login'))
#     response.delete_cookie('last_login')
#     return response

def logout_user(request): #
    logout(request) #
    
    # Cek apakah ini permintaan AJAX POST
    if request.method == 'POST':
        #
        response = JsonResponse({"status": "SUCCESS", "message": "Logout successful!"}, status=200)
    else:
        # Traditional GET/Redirect Logout
        response = HttpResponseRedirect(reverse('main:login')) #

    response.delete_cookie('last_login') #
    return response #

@csrf_exempt
@require_POST
def login_ajax(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"status": "ERROR", "message": "Invalid JSON format."}, status=400)

    form = AuthenticationForm(data=data)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        
        # Buat response dan set cookie (seperti di view aslinya)
        response = JsonResponse({"status": "SUCCESS", "message": "Login successful!"}, status=200)
        response.set_cookie('last_login', str(datetime.datetime.now())) # Perlu import datetime

        return response
    
    # Non-field errors (misalnya: username/password salah)
    errors = dict(form.errors.items())
    return JsonResponse({"status": "ERROR", "message": "Invalid credentials or missing input.", "errors": errors}, status=400)

@csrf_exempt
@require_POST
def register_ajax(request):
    try:
        # Mengambil data dari JSON body, karena AJAX modern sering mengirim JSON
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"status": "ERROR", "message": "Invalid JSON format."}, status=400)

    form = UserCreationForm(data)

    if form.is_valid():
        user = form.save()
        messages.success(request, 'Your account has been successfully created! You can now log in.')
        return JsonResponse({"status": "SUCCESS", "message": "Account created successfully."}, status=201)
    
    # Ambil error per field untuk ditampilkan
    errors = dict(form.errors.items())
    return JsonResponse({"status": "ERROR", "message": "Failed to create account. Please check your input.", "errors": errors}, status=400)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
    
@csrf_exempt
@login_required(login_url='/login') # Pastikan user login untuk membuat produk
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            # Mengambil data dari JSON body
            data = json.loads(request.body)
            
            # Membersihkan data teks menggunakan strip_tags
            name = strip_tags(data.get("name", ""))
            description = strip_tags(data.get("description", ""))
            brand = strip_tags(data.get("brand", ""))
            
            # Mengambil data lain dari JSON
            price = int(data.get("price", 0))
            category = data.get("category", "lain") # 'lain' sebagai default
            thumbnail = data.get("thumbnail", "")
            is_featured = bool(data.get("is_featured", False))
            stock = int(data.get("stock", 0))
            # Handle rating (bisa jadi float atau None)
            rating_raw = data.get("rating", None)
            rating = float(rating_raw) if rating_raw is not None else None

            user = request.user
            
            # Validasi sederhana
            if not name or price <= 0:
                return JsonResponse({"status": "error", "message": "Nama dan Harga yang valid diperlukan."}, status=400)

            # Membuat objek Product baru
            new_product = Product(
                name=name,
                price=price,
                description=description,
                category=category,
                thumbnail=thumbnail,
                is_featured=is_featured,
                stock=stock,
                rating=rating,
                brand=brand,
                user=user
            )
            new_product.save()
            
            # Sukses
            return JsonResponse({"status": "success", "message": "Produk berhasil dibuat."}, status=201) # 201 Created

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except (ValueError, TypeError) as e:
            return JsonResponse({"status": "error", "message": f"Invalid data type: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"An unexpected error occurred: {str(e)}"}, status=500)

    else:
        # Hanya izinkan metode POST
        return JsonResponse({"status": "error", "message": "Metode POST saja yang diizinkan"}, status=405)