from django.db import models
from ckeditor.fields import RichTextField

# Defino el modelo principal.
class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='pages/')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
