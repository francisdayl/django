from django.shortcuts import render
from core.forms import SignUpForm

from item.models import Category,Item
import requests
# Create your views here.

def index(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)[0:6]

    return render(request,'core/index.html',{'categories':categories , 'items':items})

def signup(request):
    form = SignUpForm()
    return render(request,'core/signup.html',{'form':form})


def contact(request):
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = posts.json()
    return render(request,'core/contact.html',{'posts':data})
