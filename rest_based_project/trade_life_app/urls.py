from django.contrib import admin
from django.urls import path
from .views import TradeAPIView

urlpatterns = [
    path('trade/', TradeAPIView.as_view()),
]