from django import forms

from .models import Post,Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(MyForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','maintext','image','boturl')
class OrderForm(forms.ModelForm):
	"""docstring for OrderForm"""
	class Meta:
		model=Order
		fields=('tgid','dops')
