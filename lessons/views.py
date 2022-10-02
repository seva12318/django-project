import json

import django.middleware.csrf
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import login as auth_login, logout as auth_logout


class LoginView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        login_form = AuthenticationForm(request, data)
        response_data = {}
        if login_form.is_valid():
            auth_login(self.request, login_form.get_user())
            response_data['result'] = 'Success!'
            response_data['message'] = 'You"re logged in'
            response_data['csrf'] = django.middleware.csrf.get_token(request)
        else:
            response_data['result'] = 'Failed'
            response_data['message'] = 'Wrong user or password'

        return JsonResponse(response_data)


class LogoutView(View):
    def post(self, *args, **kwargs):
        auth_logout(self.request)
        return JsonResponse({

        })


class CheckLoginView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            "authenticated": bool(self.request.user and self.request.user.is_authenticated),
            "username": self.request.user.username if self.request.user else "",
            'csrf': django.middleware.csrf.get_token(request),
            'is_superuser': self.request.user.is_superuser
        })
