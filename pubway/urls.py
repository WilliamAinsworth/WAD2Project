from django.conf.urls import url
from pubway import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #User authentication
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #Subcrawl
    url(r'^subcrawl/new/$', views.new_subcrawl, name='new_subcrawl'),
    url(r'^stationPage/', views.stationPage, name='stationPage'),
]
