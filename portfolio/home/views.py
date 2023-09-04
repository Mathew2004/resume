from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Skills, About, Project,Contact

# Create your views here.
def Home(request):
    skill = Skills.objects.all()
    projs = Project.objects.all().order_by('id')[:3]

    return render(request, 'home/index.html',{
        'skills':skill,
        'projs': projs
    })

def about(request):
    about = About.objects.all().first()

    return render(request, 'home/about.html',{
        'about':about
    })

def projects(request):
    projs = Project.objects.all()

    return render(request, 'home/projects.html',{
        'projs':projs
    })

def contact(request):

    if(request.method == "POST"):
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']

        contact = Contact(name=name, email=email, msg=msg)
        contact.save()
        messages.success(request, "Your message has been successfully sent")

    return render(request, 'home/contact.html')