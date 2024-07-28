from django.shortcuts import render

# Create your views here.
def stockpicker(request):
    return render(request, 'base/stockpicker.html')

def stocktracker(request):
    return render(request, 'base/stocktracker.html')