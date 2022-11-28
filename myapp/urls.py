from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Add.as_view(), name = 'add'),
    path('show/', views.Show.as_view(), name = 'show'),
    path('edit/<int:id>/', views.Edit.as_view(), name = 'edit'),
    path('delet/<int:id>/', views.Delete.as_view(), name = 'delete'),
]
