from django.contrib import admin
from django.urls import path, include  # 'path' yahan se aata hai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),  # Ye notes app ki urls ko connect karta hai
]