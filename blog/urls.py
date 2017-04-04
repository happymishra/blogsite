from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^api/bloglist/$', views.post_list, name='post_list'),
    url(r'^api/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^index/$', views.post_list_page, name='post_list_page'),
    url(r'^api/save/', views.save_edit_blog, name='save_edit_blog'),
    url(r'^api/delete/(?P<pk>\d+)/$', views.delete_blog, name='delete_blog'),
    url(r'^create/$', views.create_blog_page, name='create_blog_page'),
    url(r'^api/create/$', views.create_blog, name='create_blog'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html', 'next_page': 'post_list_page'},
        name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^login_error/$', views.login_error, name='login_error'),

    # Reset password url
    url(r'^password_reset/$', auth_views.password_reset, {'post_reset_redirect': '/blog/password_reset/mailed/'},
        name='password_reset'),
    url(r'^password_reset/mailed/$', auth_views.password_reset_done),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url('^password_reset/complete/$', auth_views.password_reset_complete),

    # Change password link

    url(r'^password_change/$', auth_views.password_change, {'post_change_redirect': '/blog/password_change/done/'},
        name='password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done),

]
