
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import signup_form,login_form
from django.contrib.auth.models import User
from django.contrib.auth    import authenticate

def base(request):

    return render(request,'myapp/base.html')


def about(requset):

    return render(requset,'myapp/about.html')

def main(request):

    return render(request,'myapp/home.html')

def login(request):
    myerror = None
    context = {'error':myerror}
    return render(request,'myapp/login.html',context)

def signup(request):

    if request.method == 'POST':

        form = signup_form(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            name=str(name).strip()
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']

            try:
                user = User.objects.get(username=name)
                myerror = "User already Exist so Please Login<br />If not register then choose other username"
                context = { 'error':myerror}
                return render(request,'myapp/login.html',context )
            except:

                u = User.objects.create_user(name,password,email)
                u.first_name=first_name
                u.last_name=last_name
                u.save()

                context = { 'name':name,'email':email,'first_name':first_name,'last_name':last_name,'message':"You Have Created your Account Successfully"}
                return render(request,'myapp/profile.html',context)



            #return HttpResponse("Name = %s<br />Email = %s<br />password = %s<br />"%(name,email,password))
        else:
            error = "Form data is invalid  Please try again "
            return render(request,'myapp/login.html',{'error':error})

    else :
        error = "Invalid Entries in Form,Please Make sure all entries are correct"
        return render(request,'myapp/login.html',{'error':error})



def profile(request):

        return render(request,'myapp/profile.html')

def adduser(request):


    if request.method == 'POST':

        form = login_form(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            name=str(name).strip()
            password=form.cleaned_data['password']

            user = authenticate(username=name,password=password)

            if user is not None:
                data=User.objects.get(username=name)
                name=data.username
                email=data.email
                first_name=data.first_name
                last_name=data.last_name
                context = { 'name':name,'email':email,'first_name':first_name,'last_name':last_name, 'message':'Welcome Back to Your Profile' }
                return render(request,'myapp/profile.html',context)
            else:
                error = "Either UserName Or Password is invalid Try Again"
                return  render(request,'myapp/login.html',{'error':error})
        else :

            error = "Invalid Entries in Form,Please Make sure all entries are correct"
            return render(request,'myapp/login.html',{'error':error})



def contact(request):

    return render(request,'myapp/contact.html')