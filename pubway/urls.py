from django.conf.urls import url
from pubway import views

urlpatterns = [
    #User authentication
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #Something else
]
