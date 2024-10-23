from django.urls import path

from college import views

urlpatterns = [
    path('test1/', views.home_page),
]
