"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('reviews/', include('reviews.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings

from product import views
from Purchased.views import purchased
from Purchased.views import delete_purchased



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('reviews/',include('reviews.urls')),
    path('main/',views.main,name='main'),
    path('<int:product_id>/',views.detail,name='detail'),
    path('<int:product_id>/delete',views.deleteprod,name='deleteprod'),

    #user
    path('signup/', views.signupuser,name='signupuser'),
    path('logout/', views.logoutuser,name='logoutuser'),
    path('login/', views.loginuser,name='loginuser'),

    #purchased - куплено
    path('purchased/',purchased,name='purchased'),
    #удаление товара пользователем
    path('delete_purchased/<int:purchased_id>/', delete_purchased, name='delete_purchased'),
    path('edit-wallet/',views.edit_wallet,name='edit_wallet'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
