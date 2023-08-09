from django.shortcuts import redirect, render
from products.forms import OrganicStoreForm
from .models import OrganicStoreModel
# Create your views here.
def home(request):
    return render(request,'base.html')

# To Store Product
def store_product(request):
    if request.method == 'POST':
        product = OrganicStoreForm(request.POST)
        if product.is_valid():
            product.save()
            # print(product.cleaned_data)
            return redirect('Showproduct')
    else:
        product = OrganicStoreForm()
            
    return render(request,'store_product.html',{'form':product})

#To Show Product
def show_product(request):
    product = OrganicStoreModel.objects.all()
    print(product)
    return render(request,'show_product.html',{'Show':product})
    
    
#To Edit Product
def edit_product(request,id):
    product = OrganicStoreModel.objects.get(pk=id)
    #automatically set all data as instance to update
    form = OrganicStoreForm(instance=product)
    if request.method == 'POST':
        form = OrganicStoreForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('Showproduct')
    return render(request,'store_product.html',{'form':form})

def delete_product(request,id):
    product = OrganicStoreModel.objects.get(pk=id).delete()
    return redirect('Showproduct')





