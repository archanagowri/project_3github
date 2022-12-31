from django.urls import path
from app1.views import *
app_name="ajith"

urlpatterns=[
    path("sam_print/",sam_print,name="sam_print"),
]