from django.shortcuts import render
from .models import Preview, Quote, Skill, Project, ContactForm, Visit
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    last_preview = Preview.objects.last()
    quotes  = Quote.objects.all()
    skills  = Skill.objects.all()
    projects  = Project.objects.all()

    # Saving Request and Ip
    
    try:
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip:
            ip = user_ip.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        Visit.objects.create(ip=ip)
    except:
        pass

#Someone opened your portfolio website at with when Home function,
    context =  {
        'preview' : last_preview,
        'quotes' : quotes,
        'skills' : skills,
        'projects' : projects
    }
    return render(request, 'homepage.html', context=context)

def contactform(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactForm.objects.create(full_name=full_name, email=email, message=message)
        return HttpResponse(f'Thank you {full_name}')
    else:
        return HttpResponse(f'Message not saved :/')