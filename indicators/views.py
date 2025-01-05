from django.shortcuts import render


def indicators(request):
    template = 'indicators.html'
    return render(request, template, {})
