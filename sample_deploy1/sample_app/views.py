from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from sample_app.models import Details
def HOME(request):
    if request.method=="POST":
        Details.objects.create(name = request.POST['name'],profile = request.POST['pf'])
        return render(request,'margins.html')
    return render(request,'margins.html')
