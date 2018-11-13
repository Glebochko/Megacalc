from django.shortcuts import render

def calc(request):
    return render(request, 'calc/calc.html', {})
