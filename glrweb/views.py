from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from . import models
from . import forms
# Create your views here.

def home_view(request):
    articles = models.Article.objects.all().prefetch_related('category')

    datos = dict(
        titulo="hola",
        articles=articles
    )
    return render(request, "home.html", datos)


class ArticlesListView(generic.ListView):
    model = models.Article
    template_name = "articles/list.html"
    context_object_name = "articles_list"


class AboutPageView(generic.TemplateView):
    extra_context = {
        "company_name": "Aperture Science"
    }
    template_name = "about.html"



def article_view(request, pk):
    context = {
        "article": models.Article.objects.get(pk=pk)
    }
    return render(request, "articles/view.html", context)


class ArticleDetailView(generic.DetailView):
    model = models.Article
    template_name = "articles/view.html"
    context_object_name = "article"


class ArticleCreateView(generic.CreateView):
    model = models.Article
    form_class = forms.ArticleCreateForm
    template_name = "articles/create.html"
    success_url = '/articles/'