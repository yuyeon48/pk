# Generated by Django 4.2.11 on 2024-07-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homst', '0007_alter_accommodation_review_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='review_score',
            field=models.FloatField(max_length=200),
        ),
    ]
