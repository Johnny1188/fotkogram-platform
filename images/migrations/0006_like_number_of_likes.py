# Generated by Django 3.0.2 on 2020-01-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='number_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]