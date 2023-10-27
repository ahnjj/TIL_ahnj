from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SignupForm, ProfileForm
from django.contrib.auth.models import User  # 프로필

# login
login = LoginView.as_view(template_name='accounts/login_form.html')

def logout(request):
    messages.success(request, '로그아웃되었습니다.')
    return  logout_then_login(request)   # logout한 다음 바로 login페이지로 넘기기
    

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, '회원가입 환영합니다.')
            next_url = request.GET.get('next','/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {'form':form})

@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필을 수정/저장했습니다.')
            return redirect('profile_edit')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile_edit_form.html", {'form':form})


# 프로필 뷰
def profile(request, pk):
    """
    프로필 기본정보
    """
    user = get_object_or_404(User, pk=pk)   # pk : user_id
    context = {'profile_user': user, 'profile_type': 'base'}
    return render(request, 'accounts/profile.html', context)