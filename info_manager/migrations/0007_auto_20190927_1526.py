# Generated by Django 2.2.3 on 2019-09-27 13:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info_manager', '0006_categorytranslation'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtranslation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemtranslation',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
