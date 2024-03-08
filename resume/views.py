from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.
def home(request):
    return render (request,"home.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    projects_show=[
    
        { 
            "title": "Job Portal System",
            "path":"images/job portal system.png" 
       },
       
       { 
            "title": "Banking management system",
            "path":"images/banking.jpg" 
       },
     
       { 
            "title": "Stock Price Prediction",
            "path":"images/stock price prediction.png" 
        },
      
       { 
            "title": "Greeting System",
            "path":"images/greet.png" 
       },
    ]
    return render(request,"projects.html",{"projects_show": projects_show})
    
def certificate(request):
    certificate_show=[
    
        { 
            "title": "ARTIFICIAL INTELLIGENCE",
            "path":"images/ai.png" 
       },
       
       { 
            "title": "BING CHAT",
            "path":"images/bing chat.png" 
       },
     
       { 
            "title": "GENERATIVE AI",
            "path":"images/generative ai.png" 
        },
      
       { 
            "title": "GENERATIVE AI-1",
            "path":"images/generative ai 1.png" 
       },   
       { 
            "title": "PYTHON",
            "path":"images/python1.png" 
       }, 
    ]
    return render(request,"certificate.html",{"certificate_show": certificate_show}) 

def contact(request):
    return render(request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb")as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found",status=404)