from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from pubway import views
from pubway.models import Place

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # User Management
    url(r'^accounts/register/$', views.register, name='register'),

    url(r'^accounts/login/$', auth_views.LoginView.as_view(
        template_name='pubway/accounts/login.html'),
        name='login'),  # Use django's included form for login
    url(r'^accounts/logout/$', views.user_logout, name='logout'),
    url(r'^accounts/profile/$', views.myprofile, name='myprofile'),
    url(r'^accounts/password/$', views.changepassword, name='changepassword'),
    url(r'^(?P<station_name_slug>[\w\-]+)/$', views.show_station, name='show_station'),
    url(r'^(?P<station_name_slug>[\w\-]+)/add_place/$', views.add_place, name='add_place'),
    url(r'^places/(?P<place_name_slug>[\w\-]+)/$', views.show_place, name='show_place'),
    url(r'^like/$', views.like_place, name='like_place'),
    # Subcrawl
    url(r'^subcrawl/new/$', views.new_subcrawl, name='new_subcrawl'),
    url(r'^subcrawl/(?P<subcrawl_name_slug>[\w\-]+)/$', views.show_subcrawl, name='show_subcrawl'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def javascript_settings():
    places = Place.objects.all()
    js_conf = {
        'places': {place.name : place.closeStation.name for place in places}
    }
    return js_conf