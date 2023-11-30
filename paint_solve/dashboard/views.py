from django.shortcuts import render ,redirect
from .models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddRecordForm  ,StockSearchForm
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
    messages.success(request,"Product Record is deleted Successfully  ")
    return redirect('home')

@login_required()
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"record add")
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
