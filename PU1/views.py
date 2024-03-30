from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate

def home(request):
    return render(request,'index.html')
def About(request):
    return render(request, "About.html")
def index(request):
    return render(request, "index.html")
def Register(request):
    return render(request, "Register.html")
def Login(request):
    return render(request, "Login.html")
def register1(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login1')
    else:
        form = UserCreationForm()
    return render(request,'register1.html',{'form':form})
def login1(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(Username = uname, Password = upass)
            return render(request, 'profile.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login1.html', {'form':form})