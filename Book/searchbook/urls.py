from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.main, name="main"),
    path('search', views.search, name="search"),
    path('delete', views.delete_all, name="delete_all"),
]
