# Generated by Django 4.1.7 on 2023-03-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoreg', '0002_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
