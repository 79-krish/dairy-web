from django.urls import path,include
from .import views

urlpatterns= [
    path("",views.first),
    path("category/<slug:val>",views.Categoriview.as_view(),name="category"),
    path("signup",views.register),
    path("signin",views.login),


]