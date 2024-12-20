# Generated by Django 5.1.1 on 2024-10-21 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
