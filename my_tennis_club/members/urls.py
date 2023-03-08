from django.urls import path
from . import views
from .views import RegisterView



urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),   
    path('members/details/<slug:slug>', views.details, name='details'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('testing/', views.testing, name='testing'),
    path('ranking/', views.ranking, name='ranking'),
    path('login_page/', views.login_page, name='login_page'),
   
    
]