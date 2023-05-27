from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modified Date")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-created"]

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(verbose_name = "Content")
    published = models.DateTimeField(verbose_name= "Publication Date", default=timezone.now())
    image = models.ImageField(verbose_name="Image", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modified Date")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created"]

    def __str__(self):
        return self.title