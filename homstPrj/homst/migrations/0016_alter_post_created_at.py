# Generated by Django 5.0.6 on 2024-07-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homst', '0015_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
