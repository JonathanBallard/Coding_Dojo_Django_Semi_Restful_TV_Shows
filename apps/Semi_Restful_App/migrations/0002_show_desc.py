# Generated by Django 3.0.3 on 2020-04-19 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Semi_Restful_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='desc',
            field=models.TextField(default='Description...'),
        ),
    ]