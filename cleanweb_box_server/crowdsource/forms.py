from django import forms

class UploadForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    IDno = forms.IntegerField()
    picture= forms.ImageField(required=False)
    latitude = forms.DecimalField(decimal_places=6, max_digits=10)
    longitude = forms.DecimalField(decimal_places=6, max_digits=10)
        
class NewUserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.EmailField()


    
