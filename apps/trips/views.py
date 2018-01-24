from django.shortcuts import render,HttpResponse, redirect

from django.contrib import messages
from ..login.models import User
from .models import Trip

def index(request):
    user= User.objects.get(id=request.session['user_id'])
    context= {
    "mytrips": Trip.objects.filter(joined_by=user),
    "otherstrips": Trip.objects.exclude(joined_by=user)
    }
    return render(request, "trips/index.html", context)

def add(request):
    return render(request, "trips/add_trips.html")

def addtrip(request):
    user_id = request.session['user_id']
    # trip_id=request.session['trip_id']
    # trip_id = request.session['trip_id']
    results = Trip.objects.validate(request.POST)
    if results['status'] == True:
        new_trip = Trip.objects.add_trip(request.POST, user_id)
        messages.success(request, 'New trip has been created!')
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/travels/')

    Trip.objects.creator(request.POST['dest'], request.session['user_id'])
    return redirect ('/travels/')
def manageerrors(request, errs):
    for err in errs:
            messages.error(request, err)

def logout(request):
    request.session.flush
    return redirect('/')
def home(request):
    return redirect('/travels/')
def destination(request,trip_id):
    trip= Trip.objects.get(id=trip_id)
    context={
        "trip":trip,
        "user":User.objects.filter(join_to__id=trip_id).exclude(id=trip.users.id),
        # exclude(id=request.session['user_id'],
    }

    return render(request,'trips/destination.html',context)

def join(request, trip_id):
    Trip.objects.joined(request.session['user_id'], trip_id)
    return redirect ('/travels/')
