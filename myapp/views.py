from django.shortcuts import render, redirect
#from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError 
from multiprocessing import context
from heapq import merge
from django.shortcuts import render
from django.http import HttpResponse
#from . models import fact,hardskill, softskill, Person,education,profession_experience,job_description #importing the class from the models.py

# Create your views here.
#from this index function we can render to the template/frontend
def index(request):
    
    return render(request,'index.html',)