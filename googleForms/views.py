from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>CI/CD Automation is Live!</h1><p>If you see this, your GitHub Action worked.</p>")