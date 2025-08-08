from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    peoples = [
        {"name": "shiva", "age": 18},
        {"name": "vijay", "age": 22},
        {"name": "prachi", "age": 20},
        {"name": "neha", "age": 17},
        {"name": "surya", "age": 18},
        {"name": "rishi", "age": 16},
        {"name": "gandu", "age": 33}
    ]
    
    text = """
    hello this is the testing of django frameworks you know there is alot of resources out there but i like django here is the reson why
    
    """
    
    vegetable = ['potato', 'pumpkin', 'tomatato']
    
    
    return render(request, "home/index.html", context= {'peoples' : peoples, 'text' : text, "vegetable": vegetable })


def contact(request):
    return HttpResponse("<h2>hello this is the contact page and enter the number?</h2>")