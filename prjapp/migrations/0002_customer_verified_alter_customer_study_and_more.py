# Generated by Django 4.2.1 on 2024-01-21 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prjapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='study',
            field=models.CharField(blank=True, choices=[('school_student', (('elementry school', 'elemebtary school'), ('high school', 'high school'), ('other', 'other'))), ('college_student', (('medical colleges', 'medical colleges'), ('engineering colleges', 'engineering colleges'), ('literary colleges', 'litrary colleges'), ('science colleges', 'science colleges'), ('other', 'other')))], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='work_field',
            field=models.CharField(blank=True, choices=[('governmental employee', (('work in government department', 'work in government department'), ('teacher', 'teacher'), ('other', 'other'))), ('free_work', (('clothes dealer', 'clothes dealer'), ('electronics dealer', 'electronics dealer'), ('librarian', 'librarian'), ('not_working', 'not_working'))), ('other', 'other')], max_length=200, null=True),
        ),
    ]
