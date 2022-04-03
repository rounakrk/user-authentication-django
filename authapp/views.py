from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# from django.db import IntegrityError
from django.db.utils import IntegrityError

# Create your views here.
def index(request):
    print(request.user)
    context = {'main':'Welcome '+request.user.username+'...'}
    if request.user.is_anonymous:
        # context['main'] = "Welcome Anonymous User..."
        # return render(request, 'index.html', context)
        return redirect("/login")
    return render(request, 'index.html', context)

def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email','')
        password = request.POST.get('password')
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        print(uname, email, password, fname, lname)
        user = User.objects.create_user(uname, email, password)
        if fname: user.first_name = fname
        if lname: user.lirst_name = lname
        try:
            user.save()
            messages.success(request, 'Account successfully created!')
        except IntegrityError as ie:
            print("Helo")
            print(IntegrityError.message())
        # popmessage = "User successfully created"
        # return render(request, 'signup.html', {'popmessage':popmessage})
    return render(request, 'signup.html')
