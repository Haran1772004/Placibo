from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>CI/CD is Working Perfectly!</h1>")