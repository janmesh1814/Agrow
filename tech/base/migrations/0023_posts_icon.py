# Generated by Django 5.0.1 on 2024-03-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_profile_address_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='icon',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
