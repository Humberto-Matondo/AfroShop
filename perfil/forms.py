from django import forms
from django.contrib.auth.models import User

from . import models


class PerfilForm(forms.ModelForm):
    class Meta: 
        model = models.Perfil 
        fields = '__all__'
        exclude = ('usuario',)

class UserForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput(), label = 'Senha', help_text= '')
    password_2 = forms.CharField(required=False, widget=forms.PasswordInput(), label = 'Confirme a senha')
    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario
    class Meta: 
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password_2')

        def clean(self, *args, **kwargs):
            data = self.data
            cleaned = self.cleaned_data
            validation_error_msgs = {}

            username_data = self.cleaned.get('username') 
            password_data = self.cleaned.get('password')
            password_2_data = self.cleaned.get('password_2')
            email_data = self.cleaned.get('email')

            usuario_bd = User.objects.filter(username=username_data).first()
            email_bd = User.objects.filter(email=email_data).first()

            error_msg_user_exists = 'Usuario ja Existe'
            error_msg_email_exists = 'E-mail ja Existe'
            error_msg_password_match = 'As senhas são diferentes'
            error_msg_password_short = 'Sua senha precisa de pelo menos 8 caracteres'
            error_msg_required_field = 'Campo obrigatorio'

            if self.usuario:
                
                if usuario_bd:
                    if usuario_data != usuario_bd.username:
                        validation_error_msgs['username'] = error_msg_email_exists

                if email_bd:
                    if email_data != email_bd.email:
                        validation_error_msgs['email'] = error_msg_email_exists

                if password_data:
                    if password_data != password_2_data:
                        validation_error_msgs['password'] = error_msg_password_match
                        validation_error_msgs['password_2'] = error_msg_password_match

                    if len(password_data) < 8: 
                        validation_error_msgs['password'] = error_msg_password_short
                
            else:
                if usuario_bd:
                    validation_error_msgs['username'] = error_msg_email_exists

                if email_bd:
                    validation_error_msgs['email'] = error_msg_email_exists

                if not password_data:
                    validation_error_msgs['password'] = error_msg_required_field
                
                if not password_2_data:
                    validation_error_msgs['password_2'] = error_msg_required_field
                    
                if password_data != password_2_data:
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password_2'] = error_msg_password_match

                if len(password_data) < 8: 
                    validation_error_msgs['password'] = error_msg_password_short
                        
            if validation_error_msgs:
                raise{forms.ValidationError(validation_error_msgs)}