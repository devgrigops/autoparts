# Generated by Django 3.2.6 on 2022-11-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_remove_good_countries'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='countries',
            field=models.ManyToManyField(to='shop.Country'),
        ),
    ]
