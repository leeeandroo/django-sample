from django.contrib import admin
from django.urls import include
from django.urls import path

from . import views

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]