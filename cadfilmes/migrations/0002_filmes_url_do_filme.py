# Generated by Django 5.0.4 on 2024-04-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadfilmes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmes',
            name='url_do_filme',
            field=models.CharField(default='vazio', max_length=500),
        ),
    ]