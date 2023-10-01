from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, "index.html")
    # return HttpResponse("this is home page")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")

    # return HttpResponse("this is service page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date = datetime.today())
        contact.save()

    return render(request, "contact.html")

    # return HttpResponse("this is contact page")
