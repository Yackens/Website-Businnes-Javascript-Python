from django.db import models

# Create your models here.
class Page(models.Model):
    key = models.SlugField(max_length=100, verbose_name="Key", default="Hello21__")
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    link = models.URLField(max_length=200, verbose_name="URL", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modified Date")

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ["title"]

    def __str__(self):
        return self.title
    