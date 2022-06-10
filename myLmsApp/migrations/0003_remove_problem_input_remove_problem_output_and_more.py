# Generated by Django 4.0.4 on 2022-06-10 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myLmsApp', '0002_module_profile_problem_grades_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='input',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='output',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='problem_grade',
        ),
        migrations.CreateModel(
            name='ProblemIO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=1000)),
                ('output', models.CharField(max_length=1000)),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myLmsApp.problem')),
            ],
        ),
    ]
