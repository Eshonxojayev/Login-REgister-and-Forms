from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
class UserLoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

class UserRegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()
        return redirect('login')
# Create your views here.
