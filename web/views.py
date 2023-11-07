from django.shortcuts import render
from . models import Project,Update,Service,Category,Testimonial
from . forms import ContactForm,CareerForm
from django.http import HttpResponse
import json
def index(request):
    context={
        "is_index" : True,
        'testimonials' : Testimonial.objects.all()

    }
    return render(request, "web/index.html",context)


def about(request):
    context={
        "is_about": True,
        'testimonials' : Testimonial.objects.all()

    }
    return render(request, "web/about-us.html",context)


def project(request):
    context={
        "is_project" : True,
        'projects' : Project.objects.all(),
        'categories' : Category.objects.all()

    }
    return render(request, "web/portfolio.html",context)


def service(request):
    context={
        "is_service" : True,
        'services' : Service.objects.all()
    }
    return render(request, "web/services.html",context)


def update(request):
    context={
        "is_update" : True,
        'updates' : Update.objects.all()
    }
    return render(request, "web/updates.html",context)


def career(request):
    if request.method == "POST":
        form = CareerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_career": True,
            "form": CareerForm(),
        }    
    return render(request, "web/career.html",context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/contact.html", context)