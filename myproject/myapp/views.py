from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            feedback.save()
            return render(request, 'success.html')
    else:
        form = FeedbackForm()
    return render(request, 'form.html', {'form': form})
