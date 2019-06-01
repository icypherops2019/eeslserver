"""
 Url config
"""
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api/', include('hbook.users.urls')),
    url(r'ev/', include('hbook.ev.urls')),
]
