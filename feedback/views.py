from django.shortcuts import get_object_or_404, render
from .forms import FeedbackForm, SendMassEmail
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
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

class SendUserEmails(FormView):
    template_name = 'feedback/send_emails.html'
    form_class = SendMassEmail
    success_url = reverse_lazy('admin:feedback_feedback_changelist')

    def form_valid(self, form):
        user_message = '{0} users emailed successfully!'.format(form.cleaned_data['receivers'].count())
        messages.success(self.request, user_message)
        form.send_email()
        return super(SendUserEmails, self).form_valid(form)

# def send_emails(request):
#     if request.method == 'POST':
#         form = SendMassEmail(request.POST)
#         context = {'form' : form}
#         if form.is_valid():
#             connection = mail.get_connection()
#             #messages = get_notific
#             context['Письма отправлены'] = True
#             return render(request,'feedback/send_emails.html', context)
#     else:
#         form = SendMassEmail()
#         return render(request, 'feedback/send_emails.html', {'form': form})
