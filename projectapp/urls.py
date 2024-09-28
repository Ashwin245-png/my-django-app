from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from projectapp.views import *
from django.urls import path, include


urlpatterns = [
    path('', signup, name='signup'),
    path('upload/', views.file_upload_view, name='file-upload'),  
    path('admin/', admin, name='admin'),
    path('home/', home, name='home'),
    path('delete-app/<id>/', delete_app, name='delete-app'),
    path('login/', user_login, name='login'),
    path('logout/', logout_page, name='logout_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
