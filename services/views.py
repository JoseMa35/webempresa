from django.shortcuts import render
from .models import Project, models

# Create your views here.
def portafolio(request):
    services = Project.objects.all()
    #return render(request,"portfolio/portfolio.html", {'projects':projects})
    return render(request,"services/services.html")
