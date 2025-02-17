from django.shortcuts import redirect
from django.urls import reverse

class SessionCheckMiddleware:
    """
    Middleware to check if a user session exists.
    If not, redirect to login page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Paths that do NOT require authentication
        public_paths = [
            reverse('account_app:login'),
            reverse('account_app:register'),
        ]

        # If user is NOT logged in and tries to access protected routes
        if not request.session.get('username') and request.path not in public_paths:
            return redirect('account_app:login')

        return self.get_response(request)
