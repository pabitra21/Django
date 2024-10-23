from django.urls import path

from college import views

urlpatterns = [
    path('test/', views.home_page, name='templates/college/index.html'),
]
