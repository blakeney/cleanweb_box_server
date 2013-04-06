from django. import forms

class SubmissionForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    boxID = forms.IntegerField()
    picture= forms.ImageField()
    
