import uuid
from django.shortcuts import render, redirect
from .models import Url
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(req):
    if req.method == 'POST':
        url = req.POST['link']
        # str() is like toString in js
        # uuid is a module that provides immutable objects
        # uuid4 generates a uuid based on randomness
        # [:5] means you will slice the string to its 5 character
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link = url, uuid = uid)
        new_url.save()
        return HttpResponse(uid)

def go(req, pk):
    url_details = Url.objects.get(uuid = pk)
    return redirect(url_details.link)