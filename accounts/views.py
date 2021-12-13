# from django.contrib import auth
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect

# # 회원가입
# def signup(request):
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 username=request.POST['username'],
#                 password=request.POST['password1'],
#                 email=request.POST['email'],)
#             auth.login(request, user)
#             return redirect('/')
#         return render(request, 'signup.html')
#     return render(request, 'signup.html')    



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})