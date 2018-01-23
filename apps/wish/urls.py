from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.wishlist, name='login_wishboard'),
    url(r'^item$', views.item, name='create_wish'),
    url(r'^show/(?P<id>\d+)$', views.show, name="item_show"),
    url(r'^join$', views.join, name='travels_join'),
    url(r'^unjoin$', views.unjoin, name='travels_unjoin'),
    url(r'^create_item$', views.create_item, name = 'item_create_wish'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove_item")
]
