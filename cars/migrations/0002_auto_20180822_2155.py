# Generated by Django 2.1 on 2018-08-22 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='end_year',
            field=models.PositiveIntegerField(default=3000),
        ),
    ]
