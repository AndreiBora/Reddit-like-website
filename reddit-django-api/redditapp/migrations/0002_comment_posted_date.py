# Generated by Django 2.1 on 2018-08-03 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('redditapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
