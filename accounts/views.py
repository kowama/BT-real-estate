from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # register new user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # form data validation
        is_not_valid = False
        if not first_name:
            is_not_valid = True
            messages.error(request, 'first name is required')
        if not last_name:
            is_not_valid = True
            messages.error(request, 'last name is required')
        if not username:
            is_not_valid = True
            messages.error(request, 'username is required')
        if not email:
            is_not_valid = True
            messages.error(request, 'email is required')
        if not password:
            is_not_valid = True
            messages.error(request, 'password is required')
        if password != password_confirm:
            is_not_valid = True
            messages.error(request, 'password and password confirm not match')
        if User.objects.filter(username=username).exists():
            is_not_valid = True
            messages.error(request, 'username already exist')
        if User.objects.filter(email=email).exists():
            is_not_valid = True
            messages.error(request, 'email address is being used')
        if is_not_valid:
            return redirect('register')
        # user data are all is valid
        user = User.objects.create_user(first_name=first_name,
                                        last_name=last_name,
                                        username=username,
                                        email=email,
                                        password=password)
        user.save()
        auth.login(request, user=user)
        messages.success(request, 'You are now logged in')

        return redirect('dashboard')

    # when get request
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            messages.error(request, 'username and password are required')
            return redirect('login')
        user = auth.authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'invalid credentials')
            return redirect('login')
        # all is OK
        auth.login(request, user)
        messages.success(request, 'you are now logged')
        return redirect('dashboard')

    # when get request
    return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are now logout")

    return redirect('index')
