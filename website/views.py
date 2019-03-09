from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.forms.widgets import TextInput, Textarea
from .models import FeedBack
# Create your views here.
from .forms import FeedbackCreate


def index(requests):
    return render(requests, 'website/index.html')


def get_feedback(request):
    appis = 0
    if request.method == 'POST':

        form = FeedbackCreate(request.POST)
        if form.is_valid():
            form.save()
            appis = 1
            return render(request, 'website/index.html', {'form': form, 'appis': appis})
    else:
        form = FeedbackCreate()
    return render(request, 'website/index.html', {'form': form, 'appis': appis})

    # widgets = {'name': TextInput(attrs={'placeholder': 'Your Name'}),
    #          'email': TextInput(attrs={'placeholder': 'Your Email'}),
    #         'subject': TextInput(attrs={'placeholder': 'Subject'}),
    #        'message': Textarea(attrs={'placeholder': 'Your Name', 'rows': 5})}
