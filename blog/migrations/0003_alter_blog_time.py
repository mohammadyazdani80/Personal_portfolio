# Generated by Django 3.2.7 on 2022-01-31 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateField(auto_now=True),
        ),
    ]
