# Generated by Django 2.1 on 2018-08-08 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redditapp', '0003_auto_20180807_1447'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('owner', 'post')},
        ),
    ]
