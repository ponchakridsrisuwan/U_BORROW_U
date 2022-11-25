from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('admin_detail/',admin_detail),
    path('admin_staff/',admin_staff),
    path('admin_user/',admin_user),
    path('admin_login/',admin_login),
]
