# Generated by Django 2.2.7 on 2020-04-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datathon', '0002_auto_20200404_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='saved_points',
            field=models.IntegerField(default=0),
        ),
    ]
