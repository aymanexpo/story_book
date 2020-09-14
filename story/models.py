from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(unique=True)
    class Meta:
        ordering=('-name',)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('story:story_category',args=[self.slug,])

class Story(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    body=models.TextField()
    des=models.TextField()
    publish=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('publish',)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('story:story_detail',args=[self.id,])