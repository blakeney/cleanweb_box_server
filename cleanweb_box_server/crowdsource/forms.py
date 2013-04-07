from django. import forms

class UploadForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    IDno = forms.PositiveIntegerField()
    picture= forms.ImageField(required=False)
    latitude = forms.DecimalField(decimal_places=6, max_digits=10)
    longitude = forms.DecimalField(decimal_places=6, max_digits=10)
        
