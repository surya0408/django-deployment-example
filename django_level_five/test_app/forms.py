from django import forms
from test_app.models import UserProfileInfo
from django.contrib.auth.models import User

class userForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ('username', 'email', 'password')
		
class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('portfolio', 'profile_pic')