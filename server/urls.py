from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core.views import attend_conference

urlpatterns = [
    path('', attend_conference, name='attend_conference'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
