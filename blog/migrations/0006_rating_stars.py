# Generated by Django 5.0.1 on 2024-01-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='stars',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]