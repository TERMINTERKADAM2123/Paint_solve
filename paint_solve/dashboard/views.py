from django.shortcuts import render ,redirect
from .models import Product , Supplier
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddRecordForm  ,StockSearchForm ,SupplierAddForm
# from .filters import ProductFilter
# Create your views here.

@login_required()
def home(request):
    
    return render(request,'dashboard/home.html',{})

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

@login_required()
def supplier(request):
    supplier = Supplier.objects.all()
    context = {'supplier':supplier,}
    return render(request,'supplier/supplier.html',context)

@login_required()
def add_supplier(request):
    if request.method == "POST":
        form : SupplierAddForm(request.POST )
        if form.is_valid():
            add_supplier = form.save()
            messages.success(request,"Supplier added Successfuly !")
            return redirect('supplier')
    else:
        form = SupplierAddForm()
    return render(request,'supplier/add_supplier.html',{'form':form})