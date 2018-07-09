from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='p10_2'),
]
