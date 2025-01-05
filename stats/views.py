from django.shortcuts import render

def stats(request):
    template = 'stats.html'
    return render(request, template, {})
