from .models import User
from django.template import RequestContext
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login/index.html')


def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    request.session['user_name'] = result.name

    messages.success(request, "Successfully registered!")
    return redirect("/travels")

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    request.session['user_name'] = result.name
    messages.success(request, "Successfully logged in!")
    return redirect('/travels')



# Create your views here.
# def success(request):
#         request.session['user_id']
#         print 1111
#         context = {
#         'user': User.objects.get(id=request.session['user_id']),
#         'allusers': User.objects.all(),
#         # 'currplan': Trip.objects.all()
#          # # Update User where friends = friendsname && user_id = 'user'
#         }

# def logout(request):
#     for key in request.session.keys():
#         del request.session[key]
#     return redirect('/')
#     # return render(request, 'reviews/success.html', context)
#     return render(request, 'login/travels.html', context)
