from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the quickfire_bulletin.")