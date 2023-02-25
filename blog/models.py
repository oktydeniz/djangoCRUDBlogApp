import uuid

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, default="", editable=False, db_index=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save()

    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    isActive = models.BooleanField(default=True)
    isHome = models.BooleanField(default=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False, default=uuid.uuid1)
    # category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save()

    def __str__(self):
        return f"{self.title}"
