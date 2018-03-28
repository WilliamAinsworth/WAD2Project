from pubway.forms import RegistrationForm, UserEditForm, SubcrawlForm, PlaceForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from pubway.models import Station, UserProfile, Place, Subcrawl

from django.http import HttpResponse, HttpResponseRedirect
#from django.core.urlresolvers import reverse #no longer supported
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#
# User Management
#

# Used to register user
def register(request):
    # Handle different requests
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Also authenticate user automatically after registering.
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'pubway/accounts/registration_form.html', {'form': form})

# Used to login user
def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
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
    else:
        return render(request, 'pubway/accounts/login.html', {})

# Used to logout user
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))

# Show User's details
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

#Used to change the user's password
@login_required
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # Update the password
            user = form.save()
            # Update the current session as well.
            update_session_auth_hash(request, user)
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
    user = request.user
    stations = Station.objects.all()
    places = Place.objects.all()
    form = SubcrawlForm()
    if request.method == 'POST':
        form = SubcrawlForm(request.POST)
        if form.is_valid():
            if user:
                sub_plcs = request.POST['sub_places_str'].split(',,')
                subcrawl = form.save(commit=False)
                subcrawl.sub_organiser = user
                subcrawl.save()
                for plc_name in sub_plcs:
                    try:
                        sub_plc = Place.objects.get(name=plc_name)
                        subcrawl.sub_places.add(sub_plc)
                    except:
                        #print(plc_name)
                        pass
                subcrawl.save()
                return show_subcrawl(request, subcrawl.sub_slug)
        else:
            print(form.errors)

    context_dict = {"form":form, "stations":stations, "places":places}
    response = render(request, 'pubway/new_subcrawl.html', context=context_dict)
    return response

def show_subcrawl(request, subcrawl_name_slug):
    try:
        subcrawl = Subcrawl.objects.get(sub_slug=subcrawl_name_slug)
    except:
        subcrawl = None
    user = request.user;
    context_dict = {"subcrawl": subcrawl, "slug": subcrawl_name_slug, "user": user}
    response = render(request, 'pubway/show_subcrawl.html', context=context_dict)
    return response

@login_required
def add_place_to_sub(request):
    plc_id = None
    if request.method == 'GET':
        plc_id = request.GET['plc_id']
        likes = 0
    if plc_id:
        plc = Place.objects.get(id=int(plc_id))
        if plc:
            likes = plc.likes + 1
            plc.save()
    return HttpResponse(likes)


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
        stationPlaces = stationPlaces.order_by('-likes')
        top_places = stationPlaces[:5]

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
        station = Station.objects.get(name=place.closeStation)
        context_dict['place'] = place
        context_dict['station'] = station

    except Place.DoesNotExist:
        context_dict = {}

    return render(request, 'pubway/placePage.html', context_dict)


@login_required
def add_place(request,station_name_slug):

    try:
        station = Station.objects.get(slug=station_name_slug)
    except Station.DoesNotExist:
        station = None

    place_form = PlaceForm()

    if request.method == 'POST':
        place_form = PlaceForm(request.POST)

        if place_form.is_valid():
            if station:
                place = place_form.save(commit=False)
                place.closeStation = station
                place.likes = 0
                place.save()
                return show_place(request, place.slug)

        else:
            print(place_form.errors)

    context_dict = {'form': place_form, 'station': station}
    reponse = render(request,'pubway/add_place.html',context_dict)
    return reponse

@login_required
def like_place(request):
    if request.method == 'GET':
        plc_id = request.GET['place_id']
        likes = 0
        if plc_id:
            plc = Place.objects.get(id=int(plc_id))
            if plc:
                likes = plc.likes + 1
                plc.likes = likes
                plc.save()
    return HttpResponse(likes)
