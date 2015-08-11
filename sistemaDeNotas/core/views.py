from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from core.forms import LoginForm, ChangePasswordForm
from core.models import User, Institucion
from django.contrib.auth import login, authenticate, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('materias_de_docente')
        else:
            form = LoginForm()
            institucion = Institucion.objects.all()
            if institucion:
                nombre_institucion = institucion[0].nombre
            else:
                nombre_institucion = "Nombre a completar"
            return render(request, 'login.html', {'form': form, 'nombre_institucion': nombre_institucion})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=User.objects.get(username= request.POST['username']), password=request.POST['password'])
            login(request, user)
            return redirect('materias_de_docente')
        else:
            return render(request, 'login.html', {'form': form})

class DocenteChangePasswordView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = ChangePasswordForm()
        return render(request, 'change_password.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = request.POST['password_1']
            user_logged = User.objects.get(username=request.user.username)
            user_logged.set_password(new_password)
            user_logged.save()
            return redirect('login')
        else:
            return render(request, 'change_password.html', {'form': form})

class DocenteResetPasswordView(View):

    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'reset_password.html')

class DocenteMateriasView(View):

    def get(self, request):
        institucion = Institucion.objects.all()
        if institucion:
            nombre_institucion = institucion[0].nombre
        else:
            nombre_institucion = "Nombre a completar"
        return render(request, 'materias.html', {'nombre_institucion': nombre_institucion})

class LogOutView(View):

    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect('login')

class ProfesorView(View):
    def get(self, request):
       return render(request, 'pantalla_profesor.html')
