# Generated by Django 3.2.3 on 2021-06-30 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]