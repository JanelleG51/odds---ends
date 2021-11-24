from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='wines'),
    path('wine/<int:wine_id>/', views.wine_detail, name='wine_detail'),
    path('cases/', views.all_cases, name='cases'),
    path('case/<int:case_id>/', views.case_detail, name='case_detail'),
    path('add_wine/', views.add_wine, name='add_wine'),
    path('add_case/', views.add_case, name='add_case'),
    path('edit_case/<int:case_id>/', views.edit_case, name='edit_case'),
    path('edit_wine/<int:wine_id>/', views.edit_wine, name='edit_wine'),
]
