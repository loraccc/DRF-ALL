# Generated by Django 5.0.1 on 2024-02-01 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_review_delete_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='stars',
        ),
        migrations.AddField(
            model_name='review',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='review',
            name='watchlist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='blog.watchlist'),
            preserve_default=False,
        ),
    ]
