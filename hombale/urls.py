from django.urls import path
from hombale.views import *
file_name="anything you want"
urlpatterns=[
    path("kgf/",kgf,name="kgf"),
    path("salaar/",slaar,name="slaar"),

]