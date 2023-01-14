# Generated by Django 4.1.5 on 2023-01-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
