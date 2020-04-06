# Generated by Django 2.2.7 on 2020-04-06 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datathon', '0007_auto_20200406_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusscore',
            name='score',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='team',
            name='points',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='teamdataset',
            name='points',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]