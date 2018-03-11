from django.conf.urls import url
from pubway import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #User Management
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^my-profile/$', views.myprofile, name='myprofile'),
    url(r'^my-profile/change-password/$', views.changepassword, name='changepassword'),
    #Subcrawl
    url(r'^subcrawl/new/$', views.new_subcrawl, name='new_subcrawl'),
    url(r'^(?P<station_name_slug>[\w\-]+)/$', views.show_station, name='show_category')
]