from django.urls import path
from .views import *

urlpatterns = [
  path('hello/', say_hello),
  path('profile/', user_profile),
  path('queries/<int:pk>/', filter_queries),
]
