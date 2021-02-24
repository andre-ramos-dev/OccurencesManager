from django.contrib.auth import get_user_model
from django.contrib.gis.db import models

from occurrences.choices import STATUS_CHOICES

User = get_user_model()


class Category(models.Model):
    type = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=150, blank=True, default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.type


class Occurrence(models.Model):
    author = models.ForeignKey(User, related_name='author_occurrences', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category_occurences', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, blank=True, default='')
    location = models.PointField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='to_validate')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Occurrence'
        verbose_name_plural = 'Occurrences'

    def __str__(self):
        return f"{self.category} - {self.description}"
