from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^list$', views.list, name="list"),
    url(r'^add$', views.add, name="add"),
    url(r'^edit$', views.edit, name="edit"),
    url(r'^delete$', views.delete, name="delete"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
]
