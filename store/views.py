from django import views
from django.db.models.base import Model
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import *
from django.views.generic import DetailView

# Create your views here.

#def index(request):
 #   data = product.objects.all()
  #  return render(request, 'index.html', {'product' : data})


def wishlist(request):
    return render(request, 'wishlist.html')


def orders(request):
    return render(request, 'order.html')


def cart(request):
    return render(request, 'cart.html')


class detail(DetailView):
    Model = product
    queryset = product.objects.all()
    template_name = 'details.html'
    context_object_name = 'details'



class index(ListView):
    Model = product
    queryset = product.objects.all()
    template_name = 'index.html'
    context_object_name = 'context'



def checkout(request):
    return render(request, 'checkout.html')