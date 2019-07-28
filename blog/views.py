from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from .models import Post,Order
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,OrderForm,MyForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import telebot
from telebot.types import Message
import requests
from telebot import types
BASE_URL='https://api.telegram.org/bot/731947153:AAETaq49IdPhGCg9YssRF6RmW3ZIjzAdX4'
TOKEN = '731947153:AAETaq49IdPhGCg9YssRF6RmW3ZIjzAdX4o'
tb = telebot.TeleBot(TOKEN)
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
# Вариант регистрации на базе класса FormView
# class MyRegisterFormView(FormView):
#     # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
#     # это UserCreationForm - стандартный класс Django унаследованный
#     form_class = UserCreationForm

#     # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
#     # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
#     success_url = "/accounts/login/"

#     # Шаблон, который будет использоваться при отображении представления.
#     template_name = "register.html"

#     def form_valid(self, form):
#         form.save()
#         # Функция super( тип [ , объект или тип ] ) 
#         # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
#         return super(MyRegisterFormView, self).form_valid(form)

#     def form_invalid(self, form):
#         return super(MyRegisterFormView, self).form_invalid(form)
@csrf_exempt
def Register(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            new_user = form.save();
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = MyForm()

    return render_to_response('register.html', {'form' : form})
def post_list(request):
    posts = Post.objects.order_by('index').all()
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            user=''
            post = form.save(commit=False)

            post.save()
            user+='Заказ:'+' \n'
            user+='Айди пользователя: '
            user+= post.tgid + ' \n'
            user+= 'Суть заказа: '
            user+= post.dops + ' \n'
            tb.send_message(-381217332, user)
            
            return redirect('post_list')
            

    else:
        form = OrderForm()
    return render(request, 'blog/post_detail.html', {'post': post},{'form': form} )

@login_required
def logout_view ( request ):
    logout ( request )
    return redirect('post_list')


def send_bot(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            user=''
            post = form.save(commit=False)

            post.save()
            user+='Заказ:'+' \n'
            user+='Айди пользователя: '
            user+= post.tgid + ' \n'
            user+= 'Суть заказа: '
            user+= post.dops + ' \n'
            tb.send_message(-381217332, user)
            
            return redirect('post_list')
            

    else:
        form = OrderForm()

    return render(request, 'blog/send_bot.html', {'form': form})
