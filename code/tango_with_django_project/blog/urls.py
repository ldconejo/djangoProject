from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(
        r'^view/(?P<slug>[^\.]+).html',
        views.view_post,
        name='view_blog_post'),
    url(
        r'^category/(?P<slug>[^\.]+).html',
        views.view_category,
        name='view_blog_category'),
    url(
        r'^add_category/$',
        views.add_category,
        name='add_category'),
    url(
        r'^category/(?P<category_name_url>\w+)/add_entry/$',
        views.add_entry,
        name='add_entry'),
    )

