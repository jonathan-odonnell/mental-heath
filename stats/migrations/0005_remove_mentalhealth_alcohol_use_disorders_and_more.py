# Generated by Django 4.2.17 on 2025-01-05 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_alter_mentalhealth_alcohol_use_disorders_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentalhealth',
            name='alcohol_use_disorders',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='drug_use_disorders',
        ),
    ]