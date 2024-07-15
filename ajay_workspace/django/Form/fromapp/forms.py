from django import forms


class InputForm(forms.Form):
    name = forms.CharField(max_length=50, label="Enter your name")
    email = forms.EmailField(label="Enter your email address")
    message = forms.CharField(widget=forms.Textarea, label="Enter your message")

    def __str__(self):
        return self.name
