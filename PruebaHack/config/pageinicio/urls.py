# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView # new
from django.urls import path
from .views import redirect_view
from . import views

urlpatterns = [
    #path('about/', AboutPageView.as_view(), name='about'), # new
    #path('', views.HomePageView,name='index')
    path('', views.home,name='home'),
    path('',views.second, name='second'),
    path('',views.bienvenidas, name='bienvenidas'),
    #path('bienvenidas/',views.bienvenidas, name='bienvenidas'),
]
 