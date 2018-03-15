from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from pubway import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #User Management
    url(r'^accounts/register/$', views.register, name='register'),

    url(r'^accounts/login/$',
        auth_views.LoginView.as_view(
        template_name='pubway/accounts/login.html'),
        name='login'),
    url(r'^accounts/logout/$', views.user_logout, name='logout'),
    url(r'^accounts/profile/$', views.myprofile, name='myprofile'),
    url(r'^accounts/password/$', views.changepassword, name='changepassword'),
    #Subcrawl
    url(r'^subcrawl/new/$', views.new_subcrawl, name='new_subcrawl'),
    url(r'^(?P<station_name_slug>[\w\-]+)/$', views.show_station, name='show_station')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)