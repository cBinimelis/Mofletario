# Generated by Django 5.1.6 on 2025-02-17 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_remove_recipe_steps_recipestep_recipe_steps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='instruction',
        ),
        migrations.AddField(
            model_name='recipestep',
            name='instruction',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
