from pubway.forms import RegistrationForm, UserEditForm, SubcrawlForm, PlaceForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from pubway.models import Station, UserProfile, Place
from django.views.generic import FormView

from django.http import HttpResponse, HttpResponseRedirect
#from django.core.urlresolvers import reverse #no longer supported
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#
# User registration
#

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'pubway/accounts/registration_form.html', {'form': form})


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>'] # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Pubway account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'pubway/accounts/login.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))

@login_required
def myprofile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('index')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'pubway/accounts/edit_profile.html', {'form': form})


@login_required
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pubway/accounts/password_change_form.html', {
        'form': form
    })

#
# Subcrawl
#
@login_required
def new_subcrawl(request):
    friends = UserProfile.objects.all() #for now, to be changed
    form = SubcrawlForm()
    user = request.user
    stations = Station.objects.all()
    context_dict = {"friends": friends, "form":form, "user":user, "stations":stations}
    response = render(request, 'pubway/new_subcrawl.html', context=context_dict)
    return response


def index(request):
    context_dict = {}
    try:
        station_list = Station.objects.all()
        #places = Place.objects.filter(closeStation=station)
        places_list = Place.objects.all()
        context_dict['stations'] = station_list
        context_dict['places'] = places_list

    except Station.DoesNotExist:
        context_dict = {}

    response = render(request, 'pubway/index.html', context_dict)
    return response

def show_station(request, station_name_slug):
    context_dict = {}
    try:
        station = Station.objects.get(slug=station_name_slug)

        stationPlaces = Place.objects.filter(closeStation=station)
        top_places = stationPlaces.objects.order_by('-likes')[:5]

        context_dict['station'] = station
        context_dict['places'] = stationPlaces
        context_dict['top_places'] = top_places

    except Station.DoesNotExist:
        context_dict = {}

    return render(request, 'pubway/stationPage.html', context_dict)

def show_place(request,place_name_slug):
    context_dict = {}
    try:
        place = Place.objects.get(slug=place_name_slug)
        context_dict['place'] = place

    except Place.DoesNotExist:
        context_dict = {}

    return render(request, 'pubway/placePage.html', context_dict)
