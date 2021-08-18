from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
# from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'login/login.html')

# Sign Up
# def signup(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#         return redirect('home')
#     else:
#         form = RegisterForm()
#         return render(request, 'signup.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/')
    return render(request, 'login/signup.html')

#Log In
# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request = request, data = request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request = request, username = username, password = password)
#             if user is not None:
#                 login(request, user)

#         return redirect('/')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'login/login.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #auth.authenticate 라는 말은 DB에서 방금전에 입력한 이 내용이 우리한테 있는 회원명단이 맞는지 확인시켜주는 함수
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:    # is not None = None이 아니라면 = 회원이라면
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login/login.html')


def logout(request):
    auth.logout(request)
    #로그아웃 시키고 홈페이지로 보내기
    return redirect('/')


def signUpPage(request):
    print("Hello")
    return render(request, 'login/signup.html')

