
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home),
    path("blogs", views.blogs, name="blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blogs_detail, name="blog_details"),
]
