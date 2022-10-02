from django.shortcuts import render

# Create your views here.
def waiting(request):
    return render(request, 'waiting.html', {})