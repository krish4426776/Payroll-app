from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView 
 

urlpatterns = [
    path('' , views.Home , name='home'),
    path('register/' , views.CreateNewUser , name='register'),
    path('addbll' ,views.AddBillForPayment , name='addbill'),

    path('login/', CustomLoginView.as_view() , name='login' ),
    path('logout/', LogoutView.as_view(next_page='login'),name= 'logout'),

    path('deleteuser/<str:pk>/' , views.DeleteUser , name='delete'),
    path('edituser/<str:pk>/' , views.Edituser , name='edit'),

    path('view' , views.Payment , name='payment'),
    path('paybill/<str:pk>/'  , views.pay , name='payy'),
  

    







]