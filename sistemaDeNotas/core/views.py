from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from core.forms import LoginForm

class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('teacher_courses')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('teacher_courses')
        else:
            return render(request, 'login.html', {'form': form})