from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import FailedLoginAttempt
from datetime import timedelta
from django.utils import timezone
# Create your views here.
# def logout_view(request):
#     logout(request)
#     return redirect((reverse_lazy('login')))

class CustomLoginView(LoginView):
    
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')  # Reemplaza con la URL a la que deseas redirigir después del inicio de sesión exitoso


    def form_invalid(self, form):
        username = form.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()

        if user:
            last_failed_attempt = FailedLoginAttempt.objects.filter(user=user).order_by('-timestamp').first()

            if last_failed_attempt:
                elapsed_time = timezone.now() - last_failed_attempt.timestamp
                if elapsed_time < timedelta(minutes=5):
                    return self.render_to_response(self.get_context_data(form=form, error_message='Demasiados intentos fallidos. Intente nuevamente en 5 minutos.'))

            FailedLoginAttempt.objects.create(user=user)
            failed_attempts = FailedLoginAttempt.objects.filter(user=user, timestamp__gte=timezone.now() - timedelta(minutes=5)).count()
            print('Número de intentos fallidos:', failed_attempts, flush=True)

            
            if failed_attempts >= 3:
                print('LIMITE DE ERRORES')
                return self.render_to_response(self.get_context_data(form=form, error_message='Demasiados intentos fallidos. Intente nuevamente en 5 minutos.'))


        return super().form_invalid(form)
