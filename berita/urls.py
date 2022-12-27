from django.contrib import admin
from django.urls import path ,include

from . views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404,handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('karya.urls')),
    
    path('', home, name='home'),
    path('base/', base, name='base'),
    path('about/', about, name='about'),
    path('berita/', berita, name='berita'),
    path('artikel/', artikel, name='artikel'),
    
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, decument_root=settings.MEDIA_ROOT)