from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.lr_app.urls')),
]
