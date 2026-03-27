from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Salam! Ye mera pehla Django page hai.</h1>")