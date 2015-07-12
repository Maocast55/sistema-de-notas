from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import LoginView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistemaDeNotas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LoginView.as_view(), name='login'),
)
