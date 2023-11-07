from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("project/", views.project, name="project"),
    path("service/", views.service, name="service"),
    path("update/", views.update, name="update"),
    path("career/", views.career, name="career"),
    path("contact/", views.contact, name="contact"),
]