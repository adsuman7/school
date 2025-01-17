# Generated by Django 3.0.6 on 2020-07-16 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20200712_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creativity', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10)),
                ('Attendence', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10)),
                ('Assignment', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10)),
                ('student_voting', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10)),
                ('staff_voting', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='teacher_subject',
            name='avg_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher_subject',
            name='class_name',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher_subject',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacherinfo'),
        ),
    ]
