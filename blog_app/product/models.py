from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} {self.content} {self.author}'