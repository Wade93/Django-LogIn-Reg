from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register_new_user$', views.register_new_user),
    url(r'^login$', views.login),
    url(r'^clear$', views.clear_session),
    url(r'^logout$', views.logout),
]