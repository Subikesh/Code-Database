# Generated by Django 3.1 on 2020-08-27 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200826_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='link',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
