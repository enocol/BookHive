from bookstore import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:book_id>/", views.book_detail, name="book_detail"),
]