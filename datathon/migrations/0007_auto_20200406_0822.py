# Generated by Django 2.2.7 on 2020-04-06 08:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datathon', '0006_bonusscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='points',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='teamdataset',
            name='points',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=4),
        ),
        migrations.AlterUniqueTogether(
            name='bonusscore',
            unique_together={('team', 'dataset', 'user')},
        ),
    ]
