from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("passowrd")

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                # raise forms.ValidationError("Password is wrong") # 전역
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            # raise forms.ValidationError("User does not exist") # 전역
            self.add_error("email", forms.ValidationError("User does not exist"))

