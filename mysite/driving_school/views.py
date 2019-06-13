from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from driving_school.models import CustomUser
import logging

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# from django.http import HttpResponse
from django.views.generic import ListView
from driving_school.models import Planning

def get_users(request):
    planning = Planning.objects.filter().order_by('date')
    return render(request, 'student.html', {'planning': planning})
