from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
    )
User = get_user_model()


class UserLoginForm(forms.Forms):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password ')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist ')
            if not user.check_password(password):
                 raise forms.ValidationError('Incorrect pass')
            if not user.is_active:
                 raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)
    
class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(lebel='Email Adress')
    email2 = forms.EmailField(lebel='Email Adress')
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    class Meta:
        model= User,
        fields = ['username','email','email2', 'password']
        
    def clean(self):
        email =self.cleaned_data.get('email')
        email2 =self.cleaned_data.get('email2')
        
        if email !=email2:
            raise forms.ValidationError('Incorrect')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email is used"
            )
            return email 