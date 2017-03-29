from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^api/bloglist/$', views.post_list, name='post_list'),
    url(r'^api/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^index/$', views.post_list_page, name='post_list_page'),
    # url(r'^detail/$', views.post_detail_page, name='post_detail_page'),
    url(r'^api/save/', views.save_edit_blog, name='save_edit_blog'),
    url(r'^api/delete/(?P<pk>\d+)/$', views.delete_blog, name='delete_blog'),
    url(r'^create/$', views.create_blog_page, name='create_blog_page'),
    url(r'^api/create/$', views.create_blog, name='create_blog'),
    url(r'^login/$', auth_views.login, {'template_name': 'blog/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html', 'next_page': 'post_list_page'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/complete/$', views.registration_complete, name='registration_complete')

]

