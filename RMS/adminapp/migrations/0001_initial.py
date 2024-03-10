# Generated by Django 5.0 on 2024-02-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=12)),
                ('phoneNumber', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('departmentId', models.CharField(max_length=30, unique=True)),
                ('departmentName', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'register_table',
            },
        ),
    ]