# Generated by Django 3.0.6 on 2020-08-10 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20200810_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffinfo',
            name='subjects',
            field=models.CharField(default='idk', max_length=100),
        ),
    ]
