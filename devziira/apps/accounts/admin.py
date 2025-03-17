from django import forms
from django.contrib.admin import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ValidationError

from devziira.apps.accounts.models import CustomUser

User = get_user_model()

class EmailOrUsernameAdminLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email/Username')

    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')


        if username_or_email and password:
            if "@" in username_or_email:
                self.user_cache = User.objects.filter(email=username_or_email).first()
            else:
                self.user_cache = User.objects.filter(username=username_or_email).first()

            if self.user_cache is None:
                raise ValidationError('Invalid username or password')
            elif not self.user_cache.check_password:
                raise ValidationError('Invalid username or password')
            elif not self.user_cache.is_active:
                raise ValidationError('This account is inactive')

            self.user_cache.backend = 'django.contrib.auth.backends.ModelBackend'

        return self.cleaned_data




class CustomAdminSite(AdminSite):
    login_form = EmailOrUsernameAdminLoginForm


custom_admin_site = CustomAdminSite(name='custom_admin')

custom_admin_site.register(CustomUser)
