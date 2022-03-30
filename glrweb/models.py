from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=100
    )


class Article(models.Model):
    title = models.CharField(
        max_length=130
    )
    content = models.TextField(
        max_length=5000
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    summary = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.title
