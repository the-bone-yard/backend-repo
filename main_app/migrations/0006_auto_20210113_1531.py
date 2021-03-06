# Generated by Django 3.1.4 on 2021-01-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_park_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='email',
            field=models.CharField(default='NO EMAIL', max_length=100),
        ),
        migrations.AddField(
            model_name='park',
            name='lat',
            field=models.FloatField(default=0.0, max_length=20),
        ),
        migrations.AddField(
            model_name='park',
            name='lng',
            field=models.FloatField(default=0.0, max_length=20),
        ),
    ]
