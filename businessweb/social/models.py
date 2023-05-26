from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(max_length=100, verbose_name="Key", unique=True)
    name = models.CharField(max_length=200, verbose_name="Name")
    url = models.URLField(max_length=200, verbose_name="URL", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modified Date")

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ["name"]

    def __str__(self):
        return self.name
