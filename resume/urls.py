
from django.urls import path
from resume import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("projects/",views.projects,name="projects"),
    path("certificate/",views.certificate,name="certificate"),
    path("contact/",views.contact,name="contact"),
    path("resume/",views.resume,name="resume")
]