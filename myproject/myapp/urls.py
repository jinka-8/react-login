from django.urls import path
from .views import login, signup, data

urlpatterns = [
    path('login/', login),
    path('signup/', signup),
    path('data/', data),
]
