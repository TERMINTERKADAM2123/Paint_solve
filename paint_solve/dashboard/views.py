from django.shortcuts import render ,redirect
from .models import Product , Supplier
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddRecordForm  ,StockSearchForm  ,SupplierAddForm
# from .filters import ProductFilter
# Create your views here.

@login_required()
def home(request):
    
    return render(request,'dashboard/home.html',{})

#product
@login_required()
def product_view(request):
    form = StockSearchForm(request.POST or None )
    prod = Product.objects.all()
    
    context = { 'prod':prod,'form':form,}
    if request.method == "POST":
        prod = Product.objects.filter(Category__icontains=form['Category'].value(),)
        context = { 'form':form, 'prod':prod,}
    # 'myFilter':myFilter,
    return render(request,'product/product.html',context)

@login_required()
def product_record(request,pk):
    product_record = Product.objects.get(id=pk)
    return render(request,'product/product_record.html',{'product_record':product_record})
    
@login_required()
def delete_record(request,pk):
    delete_it = Product.objects.get(id=pk)
    delete_it.delete()
    delete_it.is_deleted = True
    messages.success(request,"Product Record is deleted Successfully  ")
    return redirect('products')

@login_required()
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Product added Successfully ")
                return redirect('products')
    return render(request,'product/add_record.html',{'form':form})

@login_required()
def update_records(request,pk):
    current_record =  Product.objects.get(id=pk)
    form = AddRecordForm(request.POST or None,instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request,"record has been updated")
        return redirect('home')
    return render(request,'product/update_records.html',{'form':form})

#supplier 
@login_required()
def supplier(request):
    supplier = Supplier.objects.all()
    context = {'supplier':supplier,}
    return render(request,'supplier/supplier.html',context)

# @login_required()
# def add_supplier(request):
#     if request.method == "POST":
#         form : SupplierAddForm(request.POST )
#         if form.is_valid():
#             add_supplier = form.save()
#             messages.success(request,"Supplier added Successfuly !")
#             return redirect('supplier')
#         else:
#             return redirect('home')
#     else:
#         form = SupplierAddForm()
#     return render(request,'supplier/add_supplier.html',{'form':form})

# @login_required()
# def add_supplier(request):
#     if request.method == "POST":
#         form = SupplierAddForm(request.POST)
#         if form.is_valid():
#             add_supplier = form.save()
#             messages.success(request, "Supplier added successfully!")
#             return redirect('supplier')
#         else:
#             # You might want to handle form errors here
#             messages.error(request, "Form is not valid. Please check the inputs.")
#             return redirect('home')
#     else:
#         form = SupplierAddForm()  # Correct indentation here
#     return render(request, 'supplier/add_supplier.html', {'form': form})

@login_required()
# def add_supplier(request):
#     if request.method == 'POST':
#         form = SupplierForm(request.POST)
#         if form.is_valid():
#             supplier = form.save(commit=False)  # Save the form data but don't commit to the database yet
#             product_data = {
#                 'Color_name': form.cleaned_data['Color_name'],
#                 'Category': form.cleaned_data['Category'],
#                 'Brand': form.cleaned_data['Brand'],
#                 'Color_code': form.cleaned_data['Color_code'],
#                 'quantity': form.cleaned_data['quantity'],
#                 'price': form.cleaned_data['price']
#             }
#             product, created = Product.objects.get_or_create(**product_data)
#             supplier.product = product  # Assign the product to the supplier
#             supplier.save()  # Now save the supplier with the associated product
#             return redirect('success')  # Redirect to a success page or URL
#     else:
#         form = SupplierForm()
    
#     return render(request, 'supplier/add_supplier.html', {'form': form})





# def add_supplier(request):
#     if request.method == "POST":
#         form = SupplierAddForm(request.POST)
#         if form.is_valid():
#             # Save the form without committing to get the Product instance
#             supplier_instance = form.save(commit=False)
            
#             # You may need to adjust the following lines based on your form structure
#             # Assuming the form contains fields related to Product (Color_name, Category, Brand)
#             product_color_name = form.cleaned_data.get('color_name')
#             product_category = form.cleaned_data.get('category')
#             product_brand = form.cleaned_data.get('brand')
#             product_color_code= form.cleaned_data.get('color_code')
#             product_quantity= form.cleaned_data.get('quantity')
#             product_price= form.cleaned_data.get('price')
            
#             # Fetch the corresponding Product instance or create a new one if not exists
#             product, created = Product.objects.get_or_create(
#                 Color_name=product_color_name,
#                 Category=product_category,
#                 Brand=product_brand,
#                 Color_code=product_color_code,
#                 quantity = product_quantity,
#                 price= product_price
#             )
            
#             # Assign the Product instance to the Supplier model
#             supplier_instance.product = product
            
#             # Save the Supplier instancequ
#             supplier_instance.save()
            
#             messages.success(request, "Supplier added successfully!")
#             return redirect('supplier')  # Replace with your actual URL name for the supplier list
#         else:
#             messages.error(request, "Form is not valid. Please check the inputs.")
#             return redirect('home')  # Replace with your actual URL name for the home page
#     else:
#         form = SupplierAddForm()
    
#     return render(request, 'supplier/add_supplier.html', {'form': form})

def add_supplier(request):
    if request.method == "POST":
        form = SupplierAddForm(request.POST)
        if form.is_valid():
            supplier_instance = form.save(commit=False)
            
            # Get product data from the form
            product_data = {
                'Color_name': form.cleaned_data['color_name'],
                'Category': form.cleaned_data['category'],
                'Brand': form.cleaned_data['brand'],
                'Color_code': form.cleaned_data['Color_code'],
                'quantity': form.cleaned_data['quantity'],
                'price': form.cleaned_data['price']
            }
            
            # Create or get the Product instance
            product, created = Product.objects.get_or_create(**product_data)
            
            # Assign the Product instance to the Supplier model
            supplier_instance.product = product
            supplier_instance.save()
            
            messages.success(request, "Supplier added successfully!")
            return redirect('supplier')  # Replace with your actual URL name for the supplier list
        else:
            messages.error(request, "Form is not valid. Please check the inputs.")
            return redirect('home')  # Replace with your actual URL name for the home page
    else:
        form = SupplierAddForm()
    
    return render(request, 'supplier/add_supplier.html', {'form': form})
