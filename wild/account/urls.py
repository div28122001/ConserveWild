from django.urls import path
from . import views


urlpatterns = [
    path("",views.registeration,name="reg"),
    path("login",views.login,name="log"),
    path("logt",views.logout,name="lgt"),
    path("profile",views.Profile,name="pro"),
        path('uprofile',views.updateprofile,name='uprofile'),
]