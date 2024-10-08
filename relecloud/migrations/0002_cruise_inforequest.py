# Generated by Django 4.2.6 on 2023-10-29 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=2000)),
                ('destinations', models.ManyToManyField(related_name='cruises', to='relecloud.destination')),
            ],
        ),
        migrations.CreateModel(
            name='InfoRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField(max_length=2000)),
                ('cruise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relecloud.cruise')),
            ],
        ),
    ]
