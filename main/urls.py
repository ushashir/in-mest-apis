from django.urls import path
from .views import *

urlpatterns = [
  path('say_hello/', say_hello),
  path('say_hello/', say_hello),
  path('profile/', user_profile),
  path('queries/<int:pk>/', filter_queries),
  # path('queries/', QueryView.as filter_queries),
]