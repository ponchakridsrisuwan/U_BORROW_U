from django.urls import path
from .views import * 

urlpatterns = [
    path('',HomePage, name="user_index"),
    path('register/',user_register, name="register"), 
    path('user_borrow/',user_borrow, name="user_borrow"), 
    path('user_borrowed/',user_borrowed, name="user_borrowed"), 
    path('user_history/',user_history, name="user_history"), 
    path('user_cart/',user_cart, name="user_cart"), 
    path('user_detail/',user_detail, name="user_detail"), 
    path('user_cart_detail_del/',user_cart_detail_del, name="user_cart_detail_del"),
    path('user_durable_articles/',user_durable_articles, name="user_durable_articles"), 
    path('user_notifications/',user_notifications, name="user_notifications"), 
    path('user_personal_info_edit/',user_personal_info_edit, name="user_personal_info_edit"), 
    path('user_personal_info/',user_personal_info, name="user_personal_info"), 
    path('user_recommend/',user_recommend, name="user_recommend"), 
    path('user_return_parcel_detail/',user_return_parcel_detail, name="user_return_parcel_detail"), 
    
    
]