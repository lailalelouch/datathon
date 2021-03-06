# Generated by Django 2.2.7 on 2020-04-04 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datathon', '0003_team_saved_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datathon.Dataset')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dataset_points', to='datathon.Team')),
            ],
            options={
                'ordering': ['dataset'],
            },
        ),
    ]
