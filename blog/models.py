from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
import views

class Admin(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
class Data(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    content = models.CharField(max_length=5000)
    slug = models.SlugField(unique=True, max_length = 200)
    number_likes = models.IntegerField(default=0)
    number_comments = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('views.post', kwargs={'slug':self.slug,},)

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Data, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural="Entries"
        ordering=["-created"]

class likes(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Data)

class comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Data)
    text = models.CharField(max_length=1000)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.user, self.date_created)


