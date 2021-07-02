from django import forms
from . import views
from . import util
from django.shortcuts import render
from django.urls import resolve
from django.http import HttpResponseRedirect, Http404
from django import forms
import markdownify, os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.views.generic.base import TemplateView
from . import util
from django.shortcuts import redirect
import random


class AddForm(forms.Form):


    tile= forms.CharField(label="Title")
    Added= forms.CharField(widget=forms.Textarea,label="")

class Editls(forms.Form):
    formtitle= forms.CharField(label="Title")
    Editform= forms.CharField(widget=forms.Textarea,label="")
