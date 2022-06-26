from curses import flash
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
    


class HtmlTemplate(models.Model):
    html_code = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.html
