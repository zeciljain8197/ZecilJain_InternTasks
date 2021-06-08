# Generated by Django 3.2.3 on 2021-06-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('team_name', models.CharField(max_length=30)),
                ('driver_number', models.IntegerField()),
                ('nationality', models.CharField(max_length=30)),
            ],
        ),
    ]
