from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)


def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phone_list.html', {'phones': phones})


def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})


def phone_list(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'price_asc':
        phones = Phone.objects.order_by('price')
    elif sort == 'price_desc':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    return render(request, 'phone_list.html', {'phones': phones})