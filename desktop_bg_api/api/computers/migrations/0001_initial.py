# Generated by Django 5.0.6 on 2024-06-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('processor', models.CharField(max_length=100)),
                ('gpu', models.CharField(max_length=100)),
                ('motherboard', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
            ],
        ),
    ]
