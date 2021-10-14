from django.contrib import admin
from django.urls import path, include
from .views import AuthorsListView
urlpatterns = [
    path("authors-list/",AuthorsListView.as_view(),name="books-api"),
]
