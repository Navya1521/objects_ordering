from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
  name = models.CharField(max_length = 100)
  my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

  def __unicode__(self):
    return str(self.name)


  class Meta(object):
    ordering = ('my_order',)

class Book(models.Model):
  title = models.CharField(max_length = 100)
  authors = models.ManyToManyField(Author, through = 'Membership',blank = False)
  my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

  def __unicode__(self):
    return str(self.title)


  class Meta(object):
    ordering = ('my_order',)

class Membership(models.Model):
  author = models.ForeignKey(Author)
  book = models.ForeignKey(Book)
  my_order = models.PositiveIntegerField(default=0, blank=False, null=False)


  class Meta(object):
    ordering = ('my_order',)
  

# Create your models here.

