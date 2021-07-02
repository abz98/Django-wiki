from django.urls import path

from . import views
import re
app_name = 'encyclopedia'
urlpatterns = [

    path("wiki", views.index, name="index"),
    path("wiki/<str:name_title>",views.ml,name="gi"),
    path("search",views.lame,name="lame"),
    path("add",views.add,name="add"),
    path("rando/", views.random_name, name="random_name"),
    path("edit/<str:selectedit>", views.modify, name="modify"),
    #path("take",views.take,name="take")
]
