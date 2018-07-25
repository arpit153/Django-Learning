from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.login_view, name='index'),
]