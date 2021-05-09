from . import views
from django.urls import path

app_name= 'class'

urlpatterns = [
    path('', views.Entrieslistview.as_view(), name="Entrieslistview"),
    path('detail/<int:pk>/', views.Entry_detail, name = "Entry_detail" ),
    path('selected_students/<int:pk>/', views.selected_students, name="selected_students"),
]