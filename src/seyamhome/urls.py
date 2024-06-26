from django.contrib import admin
from django.urls import path, include
from auth import views as auth_views
from .views import (
    home_view,
    about_view,
    pw_protected_view,
    user_only_view,
    staff_only_view,
)

urlpatterns = [
    path("", home_view, name='home'), #index page -> root page
    path("login/", auth_views.login_view),
    path("register/", auth_views.register_view),
    path("about/", about_view),
    path("hello-world/", home_view),
    path("hello-world.html", home_view),
    path('accounts/', include('allauth.urls')),
    path('protected/user-only/', user_only_view),
    path('protected/staff-only/', staff_only_view),
    path('protected/', pw_protected_view),
    path("admin/", admin.site.urls),
]
