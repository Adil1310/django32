from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Feedback', widget=forms.Textarea)