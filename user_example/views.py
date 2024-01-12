from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create youdef r views here.

@never_cache
def index(request):
    return render(request, 'user_example/index.html')




