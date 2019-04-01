
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField()
    tag = models.CharField(null=True, max_length=100)
    slug = models.SlugField(default='')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Article(models.Model):
  def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug, 'id':self.id})
 
   