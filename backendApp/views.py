from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import RequestsMade

def index(request):
    request_list = RequestsMade.objects.all().order_by('-created_at')[:10]
    context = {'request_list': request_list}
    return render(request, 'requestsmade/index.html', context)