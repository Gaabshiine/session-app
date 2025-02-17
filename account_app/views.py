from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('account_app:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('account_app:register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('account_app:login')

    return render(request, 'account_app/register.html')


from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = user.username  # Store session data
            messages.success(request, "Login successful!")
            return redirect('account_app:dashboard')
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'account_app/login.html')





def dashboard_view(request):
    username = request.session.get('username', None)
    session_expiry = request.session.get_expiry_date()

    context = {
        'username': username,
        'session_expiry': session_expiry
    }
    return render(request, 'account_app/dashboard.html', context)





def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('account_app:login')



def profile_view(request):
    username = request.session.get('username', None)
    session_expiry = request.session.get_expiry_date()

    context = {
        'username': username,
        'session_expiry': session_expiry
    }
    return render(request, 'account_app/profile.html', context)

