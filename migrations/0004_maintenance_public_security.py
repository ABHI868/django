# Generated by Django 2.0 on 2018-09-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sangaria', '0003_auto_20180913_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('availability', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('band', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
            ],
        ),
    ]