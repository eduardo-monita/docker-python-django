from django.conf.urls import url
from example_app.views import client_list, client_detail

urlpatterns = [
    url(r'^api/client/$', client_list),
    url(r'^api/client/(?P<client_id>\d+)/$', client_detail),
]