# Generated by Django 5.0.1 on 2024-02-01 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rating_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='stars',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]