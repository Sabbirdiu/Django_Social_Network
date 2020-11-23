
from django.urls import path
from .views import my_profile_view

urlpatterns = [
    path('profile/',my_profile_view),
 
]