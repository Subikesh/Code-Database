# Generated by Django 3.1 on 2020-08-25 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('link', models.URLField(null=True)),
                ('difficulty', models.TextField(max_length=10)),
                ('Other', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('question', models.ManyToManyField(to='main.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=20)),
                ('program', models.TextField(null=True)),
                ('notes', models.TextField(null=True)),
                ('link', models.URLField(null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question', verbose_name='Question')),
            ],
        ),
    ]
