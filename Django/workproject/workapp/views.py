from django.shortcuts import render
from .models import Project
# Create your views here.
def index(request):

    return render(request,'en/public/index.html')
"""
view for index page
"""

def page(request):

    
    all_projects = Project.objects.all()

    return render(request,'en/public/index.html',{'action':"all project",'all_projects':all_projects })




































"""
    new_project = Project(title="Tasks Manager with Django",description="Django project to getting start with django easily.",client_name="Me")
    new_project.save()
    return render(request,'en/public/index.html',{'action':'save database of model'} )
"""

"""



    my_variable = "Hello World!!"

    Years_old = 15

    array_city_capitale = [ "Paris", "London", "Washington"]

    return render(request,'en/public/index.html',{ "my_var":my_variable,"Years":Years_old,"array_city":array_city_capitale })


def myindex(request):

    my_variable = "HI World!!"
     
    Years_old = 19

    array_city_capitale = [ "Delhi", "London", "Washington"]

    return render(request,'en/public/index.html',{ "my_var":my_variable,"Years":Years_old,"array_city":array_city_capitale }) """
