from django.shortcuts import get_object_or_404, render
import datetime
from .models import Feedback
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        q = Feedback.objects.create(
            name = request.POST['username'],
            phone = request.POST['phone_number'],
            email = request.POST['email'],
            organization = request.POST['company'],
            message = request.POST['message'],
        )
        return HttpResponse("Thanks, your message has been sent")
    else:
        context = { }
        return render(request, 'feedback/index.html', context)
