from django import forms
from captcha.fields import CaptchaField
class LoginForm(forms.Form):
    name=forms.CharField(max_length=200,required=True,label="用戶名",widget=forms.TextInput(attrs={"autofocus":""}))
    password=forms.CharField(max_length=200,label="密碼",widget=forms.PasswordInput(attrs={'class':"a","required":"",'placeholder':"xx"}))
    captcha=CaptchaField(label="验证码")


class RegisterForm(forms.Form):
    gender=(("male","男"),("female","女"))
    name=forms.CharField(max_length=200,label="用户名")
    password1=forms.CharField(max_length=200,label="密码",widget=forms.PasswordInput)
    password2=forms.CharField(max_length=200,label="重复密码",widget=forms.PasswordInput)
    sex=forms.ChoiceField(label="xingbie",choices=gender)
    email=forms.EmailField(label="youxiang",widget=forms.EmailInput)
    captcha=CaptchaField(label="验证码")