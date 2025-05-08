from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def Test(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def Users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})