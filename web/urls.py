from django.urls import path
from .views import (Index_View, Login_View, Register_View, Log_OutView, Team_View, Testimonial_View, Service_View, Offer_View,
                    Feature_View, FAQ_View, Contact_View, Blog_View, Course_View, Error_View, CoursedetailView)

urlpatterns = [
    path('', Index_View.as_view(), name='index'),
    path('login/', Login_View.as_view(), name='login'),
    path('register/', Register_View.as_view(), name='register'),
    path('logout/', Log_OutView.as_view(), name='logout')
]