from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
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
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        #import pdb
        #pdb.set_trace()
        return reverse('views.post', kwargs={'slug':self.slug,},)

    def save(self , *args , **kwargs):
        if self.slug == "":
            self.slug=self.title
        super(Data, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural="Entries"
        ordering=["-modified"]
