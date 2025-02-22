from django.urls import path
from .views import register_view, login_view, dashboard_view, logout_view, profile_view

app_name = 'account_app'
urlpatterns = [
    path('register/', register_view, name='register'),
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),  # New Profile Page
    path('logout/', logout_view, name='logout'),
]

