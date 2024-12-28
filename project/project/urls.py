from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings

from product import views
from Purchased.views import purchased
from Purchased.views import delete_purchased
from channel.views import chat_room
# from product.views import SignupView, CustomTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('reviews/',include('reviews.urls')),
    path('main/',views.main,name='main'),
    path('<int:product_id>/',views.detail,name='detail'),
    path('<int:product_id>/from',views.payform,name='payform'),
    # path('<int:product_id>/delete',views.deleteprod,name='deleteprod'),
    #user
    path('signup/', views.signupuser,name='signupuser'),
    path('logout/', views.logoutuser,name='logoutuser'),
    path('login/', views.loginuser,name='loginuser'),

    path('auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
    path('account/', include('account.urls')),
    # path('signup/', SignupView.as_view(), name='signup'),
    # path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    #purchased - куплено
    path('purchased/',purchased,name='purchased'),
    #удаление товара пользователем
    path('delete_purchased/<int:purchased_id>/', delete_purchased, name='delete_purchased'),

    path('chat/<str:room_name>/', chat_room, name='chat_room'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
