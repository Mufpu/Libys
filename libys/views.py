from django.shortcuts import render

def catalog(request):
    return render(request, 'Catalog.html')

def new_catalog(request):
    return render(request, 'NewCatalog.html')

def product(request):
    return render(request, 'Product.html')