from django.shortcuts import render


def faqs(request):
    template = 'faqs.html'
    return render(request, template, {})
