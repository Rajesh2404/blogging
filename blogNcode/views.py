from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

from blogNcode.forms import BlogForm
from blogNcode.models import writeBlog


# Create your views here.
def index(request):
    blogs = writeBlog.objects.all().order_by('-date')
    return render(request, 'index.html', {'blogs': blogs})
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        mailerID = request.POST['email']
        message = request.POST['message']
        send_mail('Contact form',
        'Mail from: ' + name + ', mailID: ' + mailerID + ', message: ' + message,
        settings.EMAIL_HOST_USER,
        ['rkrajesh.rout2404@gmail.com'],
        fail_silently=False)
    return render(request, 'contact.html')
def NewBlog(request):
    form = BlogForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                return redirect('/NewBlog')
            except:
                pass
        else:
            form = BlogForm()
    
    return render(request, 'NewBlog.html', {'form' : form})   

