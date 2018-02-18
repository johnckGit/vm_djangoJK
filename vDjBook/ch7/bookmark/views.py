# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
# Create your views here.


class BookmarkLV(ListView):
	
	# class variable
	model=Bookmark



class BookmarkDV(DetailView):

	# class variable
	model=Bookmark
