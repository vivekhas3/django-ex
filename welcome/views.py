import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from project.settings import BASE_DIR
# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = {}
        return context
def download(request):
    with open(BASE_DIR + '/static/VivekSoundrapandi.pdf', 'r') as pdf:                                                            
        response = HttpResponse(pdf.read(),content_type='application/pdf')                                                           
        response['Content-Disposition'] = 'attachment; filename=VivekSoundrapandi.pdf'                                               
        return response   
