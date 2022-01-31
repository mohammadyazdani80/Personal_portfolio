# Generated by Django 3.2.7 on 2022-01-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('describtion', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='portdolio/image/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]