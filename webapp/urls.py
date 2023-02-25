from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('task/<pk>/', views.detail_view, name='detail'),
    path('task/update/<pk>/', views.update_view, name='update'),
    path('create/', views.create_view, name='create'),
    path('task/delete/<pk>/', views.delete_view, name='delete'),
    path('category/create', views.category_create_view, name='category_create')
]
