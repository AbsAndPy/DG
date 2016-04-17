from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.models3d, name='models3d'),
    url(r'^wanderers/$', views.wanderers_index, name='wanderers_index'),

]
