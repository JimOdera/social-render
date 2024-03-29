from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    # USER AUTHENTICATION
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
]
