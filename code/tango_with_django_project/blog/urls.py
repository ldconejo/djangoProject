from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(
        r'^category/(?P<category_name_url>\w+)/(?P<slug>\w+)/delete_post/$',
        views.delete_post,
        name='delete_post'),
    url(
        r'^category/(?P<category_name_url>\w+)/(?P<slug>\w+)/edit_post/$',
        views.edit_post,
        name='edit_post'),
    url(
        r'^category/(?P<slug>\w+)/$',
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
    url(
        r'^category/(?P<category_name_url>\w+)/(?P<slug>\w+)',
        views.view_post,
        name='view_blog_post'),
    )

