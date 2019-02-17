import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404

from products.models import Product
from products.forms import ProductModelForm


def product_list_view(request):
    # with open('products/fixtures/data/data.json') as file:
    #     data = json.load(file)
    data = Product.objects.all()
    return render(
        request,
        'products/index.html',
        {'object_list': data}
    )


def product_detail_view(request, pk):
    # with open('products/fixtures/data/data.json') as file:
    #     data = json.load(file)
    data = Product.objects.get(pk=pk)

    return render(
        request,
        'products/detail.html',
        {'object': data}
        # {'object': data[idx]}
    )


def product_create_view(request):
    form = ProductModelForm()
    success_url = reverse('products:list')

    if request.method == 'POST':
        form = ProductModelForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'products/create_prod.html',
        {'form': form}
    )


def product_update_view(request, pk):
    # try:
    #     obj = Product.objects.get(pk=pk)
    # except Exception as err:
    #     raise Http404
    obj = get_object_or_404(Product, pk=pk)

    form = ProductModelForm(instance=obj)
    success_url = reverse('products:list')

    if request.method == 'POST':
        form = ProductModelForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'products/update_prod.html',
        {'form': form}
    )