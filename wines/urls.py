from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='wines'),
    path('cases/', views.all_cases, name='cases'),

]
