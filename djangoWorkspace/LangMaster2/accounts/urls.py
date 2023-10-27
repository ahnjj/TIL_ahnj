from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required  # 프로파일


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path("signup/", views.signup, name='signup'),
    path("edit/", views.profile_edit, name='profile_edit'),
    path('profile/<int:pk>', views.profile, name='profile'),
]