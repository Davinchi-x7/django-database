# Generated by Django 4.1.7 on 2023-03-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoreg', '0005_student_city_alter_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]