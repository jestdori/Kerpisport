from django.shortcuts import render

# Create your views here.
def agency(request):
    return render(request, 'home/index.html')
