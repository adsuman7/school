# Generated by Django 3.0.6 on 2020-08-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_attendence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='feepay_date',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='salarypay_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
