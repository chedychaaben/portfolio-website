from django.shortcuts import render
from .models import Preview, Quote, Skill, Project

# Create your views here.
def homepage(request):
    last_preview = Preview.objects.last()
    quotes  = Quote.objects.all()
    skills  = Skill.objects.all()
    projects  = Project.objects.all()
#Someone opened your portfolio website at with when Home function,
    context =  {
        'preview' : last_preview,
        'quotes' : quotes,
        'skills' : skills,
        'projects' : projects
    }
    return render(request, 'homepage.html', context=context)