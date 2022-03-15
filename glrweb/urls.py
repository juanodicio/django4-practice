
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('articles/', 
        views.ArticlesListView.as_view(), 
        name="articles_list"),
    path("about/", views.AboutPageView.as_view(),
        name="about_page"),
    path('articles/view/<int:pk>',
        views.ArticleDetailView.as_view(),
        name="article_detail"),
    path('articles/create', 
        views.ArticleCreateView.as_view(),
        name="article_create"),
    path('articles/<int:pk>', 
        views.article_view, name='article_view')
]