# Generated by Django 3.2.6 on 2022-11-20 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0017_good_countries'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
    ]
