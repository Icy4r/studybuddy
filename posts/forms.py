from django import forms

class PostForm(forms.Form):
    name = forms.CharField(max_length=30)
    title = forms.CharField(max_length=30)
    location = forms.CharField(max_length=300)
    message = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter your message here...'})
    )
    date = forms.DateTimeField()
