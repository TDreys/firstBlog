# Generated by Django 2.2.13 on 2020-07-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20200723_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(max_length=200)),
                ('startDate', models.CharField(max_length=200)),
                ('endDate', models.CharField(max_length=200)),
                ('subjects', models.TextField()),
            ],
        ),
    ]
