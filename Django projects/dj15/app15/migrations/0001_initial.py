# Generated by Django 3.1 on 2020-12-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=70)),
                ('mobile_no', models.IntegerField()),
            ],
        ),
    ]
