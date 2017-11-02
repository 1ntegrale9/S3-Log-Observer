from django.conf.urls import url
from . import views

app_name = 's3log'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
]
