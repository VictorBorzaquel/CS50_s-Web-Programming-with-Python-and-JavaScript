from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="hello/index.html"),
    path("<str:name>", views.users, name="users"),
    path("victor", views.victor, name="victor"),
]