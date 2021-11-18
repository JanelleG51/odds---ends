from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='wines'),
    path('wine/<wine_id>', views.wine_detail, name='wine_detail'),
    path('cases/', views.all_cases, name='cases'),
    path('case/<case_id>', views.case_detail, name='case_detail'),
]
