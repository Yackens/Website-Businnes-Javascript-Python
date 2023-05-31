from django.db import models
from ckeditor import fields

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    content = fields.RichTextField(verbose_name="Content", )
    order = models.SmallIntegerField(verbose_name="Order", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modified Date")

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title