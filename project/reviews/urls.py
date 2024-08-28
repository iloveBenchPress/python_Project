from django.urls import path
from . import views

urlpatterns = [
    path('',views.reviews,name='todos'),
    # path('<int:blog_id>',views.detail,name='detail'),
]