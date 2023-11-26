# Generated by Django 4.2.6 on 2023-11-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_1_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]