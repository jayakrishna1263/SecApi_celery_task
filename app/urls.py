from django.urls import path
from .views import fetchApi
urlpatterns = [
    path('fetch/', fetchApi),
]