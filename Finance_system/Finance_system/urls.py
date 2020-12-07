from django.urls import include, path
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('^', include('micro_admin.urls', namespace='micro_admin')),
    path('dashboard/', include('savings.urls', namespace='savings')),
    path('dashboard/', include('loans.urls', namespace='loans')),
    path('finance/', include('core.urls', namespace='core')),
    path('admin/', include(admin.site.urls)),

]
