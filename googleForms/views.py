from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>CI/CD Pipeline & Django Site are Live! HI</h1>")