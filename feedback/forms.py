from django.forms import ModelForm
from .models import Feedback
from django import forms

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
    emails = forms.ModelMultipleChoiceField(label="Кому",
                                           queryset=Feedback.objects.only('email'),
                                           widget=forms.SelectMultiple(),
                                           )