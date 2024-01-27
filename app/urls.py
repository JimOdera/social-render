from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/<int:id>/<slug>/', views.post_detail, name='post_detail'),
    path('post_create/', views.post_create, name="post_create"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
