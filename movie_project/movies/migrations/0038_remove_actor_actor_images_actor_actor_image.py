# Generated by Django 5.0.4 on 2024-10-13 02:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0037_alter_actor_actor_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='actor_images',
        ),
        migrations.AddField(
            model_name='actor',
            name='actor_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actor', to='movies.personimage'),
        ),
    ]
