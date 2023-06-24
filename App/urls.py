from django.urls import path
from . import views

urlpatterns=[

    path('musicurl/',views.musicview,name='music'),
    path('bhartnatyamurl/',views.bharatanatyamview,name='bharatanatyam'),
    path('westerndanceurl/',views.westerndanceview,name='gallery'),
    path('kuchipudiural/',views.kuchipudiview,name='kuchipudi'),
    path('guitarurl/',views.guitarview),
    path('keyboardurl/',views.keyboardview),
    path('videourl/',views.videoview)
   ]