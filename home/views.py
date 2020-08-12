from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    context = {'name':'Keerthi', 'course':'Django'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        print("yes post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']
        print(name, email, phone, description)
        contact = Contact(name=name, email=email, phone=phone, description=description)
        contact.save()
        print("data has been written to the db")
        
    return render(request, 'contact.html')

