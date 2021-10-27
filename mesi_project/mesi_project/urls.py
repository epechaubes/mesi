from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('board/', include('board.urls', namespace='board')),
    path('login/', include('login.urls', namespace='login')),
    path('admin/', admin.site.urls),
]