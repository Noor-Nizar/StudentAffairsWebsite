# Generated by Django 4.0.4 on 2022-05-24 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_student_genderm_remove_student_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(default='', max_length=30),
        ),
    ]
