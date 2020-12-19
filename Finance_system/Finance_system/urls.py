from django.urls import include, path
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('', include('micro_admin.urls')),
    path('dashboard/', include('savings.urls')),
    path('dashboard/', include('loans.urls')),
    path('finance/', include('core.urls')),
    path('admin/', admin.site.urls),

]
