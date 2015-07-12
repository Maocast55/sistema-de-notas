from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from core.forms import LoginForm
from core.models import User
from django.contrib.auth import login, authenticate, logout

class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('materias_de_docente')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=User.objects.get(username= request.POST['username']), password=User.objects.get(username= request.POST['password']))
            login(request, user)
            return redirect('materias_de_docente')
        else:
            return render(request, 'login.html', {'form': form})

class DocenteResetPasswordView(View):

    def get(selfs, request):
        return render(request, 'reset_password.html')

class DocenteMateriasView(View):

    def get(self, request):
        import pdb;pdb.set_trace()

class LogOutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')