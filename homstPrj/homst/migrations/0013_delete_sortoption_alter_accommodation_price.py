# Generated by Django 4.2.11 on 2024-07-03 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homst', '0012_sortoption'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SortOption',
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='price',
            field=models.PositiveIntegerField(max_length=200),
        ),
    ]
