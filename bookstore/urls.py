

import os
from . views import index
from bookstore import views
from django.urls import path


urlspartterns = [
    path("", views.index, name="index"),
]