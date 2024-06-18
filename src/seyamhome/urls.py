from django.contrib import admin
from django.urls import path

from.views import homea_page_view

urlpatterns = [
    path("", homea_page_view),  #index-page
    path("hello-world/", homea_page_view),
    path("hello-world.html", homea_page_view),
    path("admin/", admin.site.urls),
]
