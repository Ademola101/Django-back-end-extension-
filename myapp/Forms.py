from django import forms
from django.contrib.auth.models import User
from .models import Profile
class SendEmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ('Subject')}))
    message = forms.CharField(widget=forms.Textarea)
    users = forms.ModelMultipleChoiceField(label="To", queryset=Profile.objects.all(),widget=forms.SelectMultiple())
  
    def send_email(self, request, queryset):
        form = SendEmailForm(initial=[queryset.values('email')])
        return render(request, 'admin/send_email.html', {'form': form})
