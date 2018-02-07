from django.shortcuts import get_object_or_404, render
from .forms import FeedbackForm, SendMassEmail
from django.core import mail

# Create your views here.

def index(request):

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip=x_forwarded_for.split(',')[-1].strip()
        else:
            ip=request.META.get('REMOTE_ADDR')
        return  ip

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        context = {"form" : form}
        if form.is_valid():
            aform = form.save(commit=False)
            aform.ip = get_client_ip(request)
            aform.save()
            context["thanks"] = True
            return render(request, 'feedback/index.html', context)
    else:
        form = FeedbackForm()
        return render(request, 'feedback/index.html', {'form': form})


def send_emails(request):
    if request.method == 'POST':
        form = SendMassEmail(request.POST)
        context = {'form' : form}
        if form.is_valid():
            connection = mail.get_connection()
            #messages = get_notific
            context['Письма отправлены'] = True
            return render(request,'feedback/send_emails.html', context)
    else:
        form = SendMassEmail()
        return render(request, 'feedback/send_emails.html', {'form': form})
