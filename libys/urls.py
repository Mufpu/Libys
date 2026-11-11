from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='home'),
    path('newbie/', views.new_catalog, name='LastCat'),
    path('see/', views.product, name='Look')
]
