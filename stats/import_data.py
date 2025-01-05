import pandas as pd
from .models import MentalHealth
from decimal import Decimal

def import_data():
    df = pd.read_csv('stats/fixtures/mental-illnesses-prevalence.csv')
    df = df.rename(columns={
        'Entity': 'country',
        'Code': 'country_code',
        'Year': 'year',
        'Schizophrenia disorders (share of population) - Sex: Both - Age: Age-standardized': 'schitzophrenia',
        'Depressive disorders (share of population) - Sex: Both - Age: Age-standardized': 'depression',
        'Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized': 'anxiety_disorders',
        'Bipolar disorders (share of population) - Sex: Both - Age: Age-standardized': 'bipolar_disorder',
        'Eating disorders (share of population) - Sex: Both - Age: Age-standardized': 'eating_disorders',
    })

    for index, row in df.iterrows():
        countries = ['Australia', 'Canada', 'France', 'Germany', 'Italy', 'Spain', 'Portugal', 'Ireland', 'Denmark', 'New Zealand', 'Norway', 'Finalnd', 'Sweden', 'Belgum', 'Iceland', 'Luxembourg', 'Singapore', 'United States', 'United Kingdom', 'Thailand', 'South Korea', 'Japan']

        if row['country'] in countries:

            i = MentalHealth.objects.create(
                country=row['country'],
                country_code=row['country_code'],
                year=row['year'],
                schitzophrenia=Decimal(row['schitzophrenia']),
                depression=Decimal(row['depression']),
                anxiety_disorders=Decimal(row['anxiety_disorders']),
                bipolar_disorder=Decimal(row['bipolar_disorder']),
                eating_disorders=Decimal(row['eating_disorders']),
            )
            i.save()

    qs = MentalHealth.objects.all()
    return qs
