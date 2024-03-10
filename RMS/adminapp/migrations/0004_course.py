# Generated by Django 5.0 on 2024-03-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_studentregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=50)),
                ('academic_year', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'course_table',
            },
        ),
    ]