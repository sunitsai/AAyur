# Generated by Django 3.1.7 on 2021-03-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=150, null=True)),
                ('Lastname', models.CharField(max_length=150, null=True)),
                ('Gender', models.CharField(max_length=15, null=True)),
                ('Email', models.EmailField(max_length=150)),
                ('Mobile', models.BigIntegerField(null=True)),
                ('Password', models.CharField(max_length=150)),
                ('State', models.CharField(max_length=150, null=True)),
                ('City', models.CharField(max_length=150, null=True)),
                ('Address', models.TextField(max_length=150, null=True)),
                ('DeviceID', models.CharField(default='abc', max_length=150)),
                ('DateJoined', models.DateTimeField(auto_now_add=True)),
                ('LastLogin', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
