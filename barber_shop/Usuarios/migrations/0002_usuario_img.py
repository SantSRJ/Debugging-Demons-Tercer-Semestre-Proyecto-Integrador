# Generated by Django 4.2.1 on 2023-06-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='img',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
