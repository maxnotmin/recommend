from django.urls import path
from . import views

app_name = "recco"

urlpatterns = [
    path('', views.home, name="recco-home"),
    path('about/', views.about, name="recco-about"),
]
