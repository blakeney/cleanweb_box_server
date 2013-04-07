from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from crowdsource.models import User, Submission
from django.utils import timezone
from crowdsource.forms import UploadForm

#display the submission form (no submission of data!)
def upload(request):
	if request.method == 'POST': # If the form has been submitted...
		data = request.POST
        form = UploadForm(data) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
        					# is_valid() is a function provided by django (don't need to overload)
            #data fields: username, password, IDno, picture, latitude, longitude
            error_string = ""
            u = User.objects.get(username = form.cleaned_data['username'])
            if u.password != form.cleaned_data['password']:
            	error_string = error_string + "/n Incorrect password."
        	else:
        		#submission fields: user, IDno, picture, sub_date, latitude, longitude
        		#creating a new submission under the user
        		u.submission_set.create(
        			IDno = form.cleaned_data['IDno'],
        			#picture = form.cleaned_data['picture'],
        			sub_date = timezone.now(),
        			latitude = form.cleaned_data['latitude'],
        			longitude = form.cleaned_data['longitude'])
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else: #display blank form
        form = UploadForm() # An unbound form
    return render(request, 'upload_form.html', {
        'form': form,
    })
    
#display thanks page
def thanks(request):
        return HttpResponse("Thank you! Congratz!")

#display submissions already uploaded (can be reached as a static webpage or as a redirect from upload page)
def display_submissions(request):

#display data associated with a user
def userpage(request, username):
