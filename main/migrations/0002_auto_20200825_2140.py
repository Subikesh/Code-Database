# Generated by Django 3.1 on 2020-08-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(to='main.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.TextField(choices=[('Hard', 'Hard'), ('Medium', 'Medium'), ('Easy', 'Easy')], max_length=10),
        ),
    ]
