from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ## Uncomment the lines below if django-admin tools are installed and shall be used
    #url(r'^admin_tools/', include('admin_tools.urls')),

    # Urls to allow password resetting
    #url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' :'django.contrib.auth.views.password_reset_done' }, name='admin_password_reset'),
    #(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    #url(r'^admin/password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        #{'post_reset_redirect' :'django.contrib.auth.views.password_reset_complete' },
        #name='password_reset_confirm'),
    #(r'^admin/password_reset/complete/$', 'django.contrib.auth.views.password_reset_complete'),

     # admin site
    url(r'^admin/', include(admin.site.urls)),
)
