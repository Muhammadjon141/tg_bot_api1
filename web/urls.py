from django.urls import path
from .views import (Index_View, Login_View, Register_View)

urlpatterns = [
    path('', Index_View.as_view(), name='index'),
    path('login/', Login_View.as_view(), name='login'),
    path('register/', Register_View.as_view(), name='register')
]