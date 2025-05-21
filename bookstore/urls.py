from bookstore import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:book_id>/", views.book_detail, name="book_detail"),
    path('edit-review/<int:review_id>/', views.edit_review, name='edit_review'),
    path("return-book/<int:book_id>/", views.return_book, name="return_book"),

    path("register/", views.user_registration, name="user_registration"),
    path("category/<str:category>/", views.category, name="book_category"),
    path("search/", views.index, name="search"), 
    path("about/", views.about, name="about"),
    path("profile/", views.profile, name="profile"),
    path("contact/", views.contact, name="contact"),
]