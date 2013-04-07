from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from crowdsource.models import User, Submission
from django.utils import timezone
from crowdsource.forms import UploadForm, NewUserForm

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
                return render(request, 'crowdsource/upload_form.html', { 'form': form, 'error_message': error_string, })
            else:
                #submission fields: user, IDno, picture, sub_date, latitude, longitude
                #creating a new submission under the user
                u.submission_set.create(
                    IDno = form.cleaned_data['IDno'],
                    #picture = form.cleaned_data['picture'],
                    sub_date = timezone.now(),
                    latitude = form.cleaned_data['latitude'],
                    longitude = form.cleaned_data['longitude'])
                return HttpResponseRedirect('/crowdsource/thanks/') # Redirect after POST

        #if form is not valid
        else:
            error_string = "Form was not valid somehow"
            return render(request, 'crowdsource/upload_form.html', { 'form': form, 'error_message': error_string, })

    else: #display blank form
        form = UploadForm() # An unbound form
        context = RequestContext(request, {
            'form': form,
        })
        return render(request, 'crowdsource/upload_form.html', context)
    
#display thanks page
def thanks(request):
    return HttpResponse("Thank you! Congratz!")

#create a user
def newUser(request):

    #if form is being posted
    if request.method == 'POST':
        data = request.POST #store the posted information in data
        form = NewUserForm(data) #form bound to POST data
        if form.is_valid():
            #create a new User object
            user = User(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                email = form.cleaned_data['email'],
                points = 0,
            )
            user.save()
            return HttpResponseRedirect('/crowdsource/thanks/')

        #if form is not valid
        else: 
            error_string = "Form was not valid somehow"
            return render(request, 'base_form.html', { 'form': form, 'error_message': error_string, })

    #if form is being displayed
    else: 
        form = NewUserForm() # An unbound form
        context = RequestContext(request, {
            'form': form,
        })
        return render(request, 'base_form.html', context)
        


def home(request):
    return HttpResponse("Home!")

#display submissions already uploaded (can be reached as a static webpage or as a redirect from upload page)
def display_submissions(request):
    pass

#display data associated with a user
def userpage(request, username):
    pass

