from django.shortcuts import redirect, render
from myapp.models import Fileupload
# Create your views here.

def index(request):
    return render(request, 'index.html')

def fileupload(request):
    a = request.POST.get('file')
    
    obj=Fileupload(file=a)
    obj.save()
    return redirect('/fileupload')