from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout   # 장고 내부에 이미 만들어진 login 기능 
from .forms import CustomUserCreationForm
from .models import User
from .forms2 import UserForm

# 로그인 : AuthenticationForm 사용
def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            login(request, form.get_user)   # form의 user로 로그인 해준다.
            return redirect('index')    # 메인 화면으로 포워딩
    else:
        form = AuthenticationForm()  # POST가 아닐 경우 빈 폼을 보여준다.

    return render(request, 'users_app/sign_in.html', {'form':form})



def sign_out(request):
    logout(request)
    return redirect('index')

# 회원가입
def sign_up(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('sign_in')  # 회원가입 후 로그인 화면으로 이동
    else:
        form = CustomUserCreationForm()

    return render(request, 'users_app/sign_up.html', {'form':form})


def sign_up2(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']
        user_address = request.POST['user_address']

        # 매개변수는 3개만 전달 가능
        # 순서 주의 : username, email, password
        user = User.objects.create_user(username, email, password)
        # 3개 외 나머지는 별도로 추가
        user.user_name = user_name
        user.user_phone = user_phone
        user.user_address = user_address
        
        user.save()

        return redirect('sign_in') # 회원가입 후 로그인화면으로 이동
    
    else:
        form = UserForm()

    return render(request, 'users_app/sign_up2.html', {'form':form})
        
        
