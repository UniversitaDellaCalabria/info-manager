# Generated by Django 2.2.3 on 2019-07-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
