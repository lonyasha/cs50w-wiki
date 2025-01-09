from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search_entry, name='search_entry'),
    path("wiki/create", views.create_entry, name='create_entry'),
    path("wiki/random", views.random_entry, name='random_entry'),
    path("wiki/<str:title>", views.get_entry, name="get_entry"),
    path("wiki/<str:title>/edit", views.edit_entry, name='edit_entry'),
]
