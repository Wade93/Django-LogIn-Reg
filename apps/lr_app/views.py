from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from .models import User


def index(request):
    if 'fname' not in request.session:
        request.session['fname'] = ""
    if 'lname' not in request.session:
        request.session['lname'] = ""
    if 'email' not in request.session:
        request.session['email'] = ""
    return render(request, 'lr_app/index.html')

def success(request):
    if request.session['fname'] == "":
        return redirect('/')
    return render(request, 'lr_app/success.html')

def register_new_user(request):
    request.session['fname'] = request.POST['fname']
    request.session['lname'] = request.POST['lname']
    request.session['email'] = request.POST['email']
    request.session['bdate'] = request.POST['bdate']
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], date_of_birth = request.POST['bdate'], password = pw_hash)
        return redirect('/success')
    

def login(request):
    errors = User.objects.log_in_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
        return redirect('/')
    else:
        request.session['user_id'] = User.objects.get(email = request.POST['email']).id
        request.session['fname'] = User.objects.get(email = request.POST['email']).first_name
        return redirect('/success')


def logout(request):
    request.session.clear()
    return redirect('/')

def clear_session(request):
    request.session.clear()
    return redirect('/')