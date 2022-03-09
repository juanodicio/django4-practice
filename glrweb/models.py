from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(
        max_length=130
    )
    content = models.TextField(
        max_length=5000
    )

    def __str__(self) -> str:
        return self.title
