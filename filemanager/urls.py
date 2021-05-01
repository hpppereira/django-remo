from django.conf.urls import url

from filemanager import path_end
from views import view

urlpatterns = (
   url(r'^abc/' + path_end, view, name='view'),
)