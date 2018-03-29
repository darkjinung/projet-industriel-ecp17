from django.conf.urls import url
from django.contrib import admin

# importing views
# we need to create views.py


from . import views

urlpatterns = [
    # define the url getdata that we have written inside form
    url(r'^showdata/', views.index),
    # defining the view for root URL
    url(r'^$', views.index),
]