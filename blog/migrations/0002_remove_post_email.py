# Generated by Django 3.2.3 on 2021-06-30 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
    ]
