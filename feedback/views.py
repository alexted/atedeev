from django.shortcuts import get_object_or_404, render
from .forms import FeedbackForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        context = {"form" : form}
        if form.is_valid():
            form.save()
            context["thanks"] = True
            return render(request, 'feedback/index.html', context)
    else:
        form = FeedbackForm()
        return render(request, 'feedback/index.html', {'form': form})
