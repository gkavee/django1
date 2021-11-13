from django.db import models
from django.urls import reverse

class Women(models.Model):
    slug = models.SlugField(max_length=111, db_index=True, unique=True, verbose_name='URL')
    title = models.CharField(max_length=255, verbose_name='заголовок')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Женщины'
        verbose_name_plural = 'Женщины'
        ordering = ['time_create', 'title']

class Category(models.Model):
    slug = models.SlugField(max_length=111, db_index=True, unique=True, verbose_name='URL')
    name = models.CharField(max_length=100, db_index=True, verbose_name='категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['id']
