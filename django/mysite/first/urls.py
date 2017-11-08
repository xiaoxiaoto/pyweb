from django.conf.urls import url,include
from first import views as first_views

urlpatterns = [
    url(r'^route/(?P<path>\w+)/$', first_views.route,name='route'),
    url(r'^edit/(?P<id>[0-9a-zA-Z\-]+)/$', first_views.edit,name='edit'),
    url(r'^addAction/$', first_views.addAction, name='addAction'),
    url(r'^deleteAction/(?P<id>[0-9a-zA-Z\-]+)$', first_views.deleteAction, name='deleteAction'),
    url(r'^editAction/(?P<id>[0-9a-zA-Z\-]+)$', first_views.editAction, name='editAction'),
    url(r'^returnJSONAction/$', first_views.returnJSONAction, name='returnJSONAction')
]
