from django.contrib import admin
from django.urls import path

from scraping.views import home_view, list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    path('list/', list_view, name='list'),
]
