from dataclasses import fields
from django.forms import ModelForm
from . import models


class ArticleCreateForm(ModelForm):

    class Meta:
        model = models.Article
        fields = ('title', 'content')