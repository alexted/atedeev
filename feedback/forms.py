from django.forms import ModelForm
from .models import Feedback
from django import forms
from django.core.mail import send_mass_mail

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ['datetime']
        widgets = {'ip': forms.HiddenInput()}

class SendMassEmail(forms.Form):
    subject = forms.CharField(
        label='Тема письма',
        widget=forms.TextInput(attrs={'placeholder': 'Укажите тему'}),
    )
    message = forms.CharField( label='Текст письма', widget=forms.Textarea(attrs={'placeholder':'Введите текст'}))
    receivers = forms.ModelMultipleChoiceField(label="Кому",
                                           queryset=Feedback.objects.only('email'),
                                           widget=forms.SelectMultiple(),
                                           )
    def send_email(self):
        receivers = self.cleaned_data['receivers']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        letter = (subject, message, "info@epsilon-design.ru", receivers)
        send_mass_mail(letter, fail_silently= False)