from django.urls import path
from app2.views import *
app_name="harar"

urlpatterns=[
    path("samantha",samantha,name="samantha"),
]