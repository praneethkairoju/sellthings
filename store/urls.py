from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from .views import index, detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index.as_view(), name='home'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('<int:pk>/', detail.as_view(), name='details'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)