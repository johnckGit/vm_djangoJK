# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


@python_2_unicode_compatible
class Post(models.Model):

	# class variables
	title = models.CharField('TITLE', max_length=50)
	slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
	description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
	content = models.TextField('CONTENT')
	create_date = models.DateTimeField('Create Date', auto_now_add=True)
	modify_date = models.DateTimeField('Modify Date', auto_now=True)

	'''
	This is just a class container with some options (metadata) attached to the mode. 
	It defines such things as available permissions, associated database table name, whether the model is abstract
	or not, singular and plural verions of the name etc.
	'''
	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'posts'
		db_table = 'my_post'
		ordering = ('-modify_date',)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('blog:post_detail', args=(self.slug,))


	def get_previous_post(self):
		return self.get_previous_by_modify_date()


	def get_next_post(self):
		return self.get_next_by_modify_date()