from django.shortcuts import render
from .models import MentalHealth
import pandas as pd


def stats(request):
    if request.GET:
        country = request.GET['country']
    else:
        country = 'United Kingdom'
    df = pd.DataFrame(MentalHealth.objects.filter(country=country).order_by('year').values()).tail(5)
    dataset = {
        'labels': df['year'].to_list(),
        'schitzophrenia': df['schitzophrenia'].to_list(),
        'bipolar_disorder': df['bipolar_disorder'].to_list(),
        'eating_disorders': df['eating_disorders'].to_list(),
        'anxiety_disorders': df['anxiety_disorders'].to_list(),
        'depression': df['depression'].to_list(),
        'country': country,
    }
    template = 'stats.html'
    return render(request, template, {'dataset': dataset})
