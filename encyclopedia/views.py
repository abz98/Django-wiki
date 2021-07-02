from django.shortcuts import render
from django.urls import resolve , reverse
from django.http import HttpResponseRedirect, Http404
from django import forms
import markdownify, os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.views.generic.base import TemplateView
from . import util
from django.shortcuts import redirect
import random
from . import forms
from .forms import AddForm
from .forms import Editls



def random_name(request):
    entries = util.list_entries() # list of wikis
    selected_page = random.choice(entries)

    return redirect('encyclopedia:gi', name_title=selected_page)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

###URL path find
def ml(request,name_title):
    return render(request, "ent/sm.html", {
        "entries": util.get_entry(name_title)

    })
#####Search
def lame(request):
    sa = request.POST['abz']
    if sa=='' or not util.get_entry(sa):
      return render(request,"notfound/nfound.html")
    return redirect('encyclopedia:gi', name_title=sa)

####save entryml
def add(request):
    if request.method=='POST' or 'GET':
        form =AddForm(request.POST)

        if form.is_valid():

            tile=form.cleaned_data["tile"]
            Added=form.cleaned_data["Added"]

            #return HttpResponseRedirect('/wiki')
        else:
           return  render(request,"add/add.html",{
             "form": AddForm(),
           })

    #tile=form.cleaned_data["tile"]
    #Added=form.cleaned_data["Added"]

    return  render(request,"add/add.html",{
      "form": form,
      "entries":util.save_entry(tile,Added)

    })

### edit page
def modify(request,selectedit):

    content = util.get_entry(selectedit)
    #content = util.get_entry(editPage)
    man={"formtitle":selectedit,"Editform":content}
    form =Editls(request.POST,man)
    data=request.POST.copy()
    if request.method =="POST" or None:

       data=request.POST.copy()
       formtitle= data.get('formtitle')
       Editform= data.get('Edit')

    formtitle="LISTS"
    Editform= "LIST"
    return render(request, "ent/edit.html",{
    "entries":util.save_entry(formtitle,Editform),
    "form":form,
    "page_title":selectedit
    })
