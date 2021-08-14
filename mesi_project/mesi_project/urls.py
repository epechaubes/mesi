from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('board/', include('board.urls', namespace='board')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
]
