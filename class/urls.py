from os import name
from . import views
from django.urls import path

app_name= 'class'

urlpatterns = [
    path('home', views.Entrieslistview.as_view(), name="home"),
    path('company_roster', views.Tablelistview.as_view(), name = 'table_view'),    
    path('detail/<int:pk>/', views.Entry_detail, name = "Entry_detail" ),
    path('selected_students/<int:pk>/', views.selected_students, name="selected_students"),
]