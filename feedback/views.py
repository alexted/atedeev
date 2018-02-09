from django.shortcuts import get_object_or_404, render, HttpResponse
from .forms import FeedbackForm, SendEmailForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
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

class SendEmailView(FormView):
    template_name = 'feedback/send_emails.html'
    form_class = SendEmailForm
    success_url = reverse_lazy('admin:feedback_feedback_changelist')

    def form_valid(self, form):
        recipients=[i.email for i in form.cleaned_data['recipients']]
        sender = form.cleaned_data['sender']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        user_message = '{0} users emailed successfully!'.format(form.cleaned_data['recipients'].count())
        messages.success(self.request, user_message)
        try:
            print(recipients)
            print(recipients)
            send_mail(subject, message, sender, recipients, fail_silently= False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return super(SendEmailView, self).form_valid(form)
