from django.urls import path
from eros.views import *
file_name="anything"
urlpatterns=[
    path("tumbbad/",tumbbad,name="tumbbad"),
    path("partner/",partner,name="partner"),

]