import logging
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from .forms import UserEmailForm, UserCodeForm
from .tasks import send_secret_code_on_email
from .cache import get_user_code
from .models import User

logger = logging.getLogger(__name__)


class AuthUserView(FormView):
    template_name = 'auth/login.html'
    form_class = UserEmailForm
    success_url = reverse_lazy('code')

    def form_valid(self, form):
        logger.info('AuthUserView: форма валидна')
        email = form.cleaned_data["email"]
        self.request.session['user_email'] = email
        form.save()
        send_secret_code_on_email.delay(email)
        return super().form_valid(form)


class AuthInputCodeView(FormView):
    template_name = 'auth/code.html'
    form_class = UserCodeForm
    success_url = reverse_lazy('quiz')

    def form_valid(self, form):
        logger.info('AuthInputCodeView: форма валидна')
        code = form.cleaned_data["code"]
        email = self.request.session["user_email"]
        verify_code = get_user_code(email)
        if code == verify_code:
            logger.info('AuthInputCodeView: коды совпадают')
            u: User = User.objects.get(email=email)
            u.email_verify = True
            u.save()
            return super().form_valid(form)
        else:
            logger.info('AuthInputCodeView: коды не совпадают')
            context = {"form": form,
                       "error_code": "Неверный код. Проверьте почту и введите код повторно"}
            return render(self.request, self.template_name, context)


class SendCode(View):
    template_name = 'auth/code.html'
    form_class = UserCodeForm

    def get(self, request, *args, **kwargs):
        logger.info('SendCode: запрос на повторную отправку кода')
        send_secret_code_on_email.delay(request.session["user_email"])
        url = reverse_lazy('code')
        return HttpResponseRedirect(url)
