from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<Album_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<Album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
    url(r'^display_favorites/$',views.display_favorites,name='display_favorites'),
    url(r'^display_favorites/remove_favorites/$',views.remove_favorites,name='remove_favorites')
    
]