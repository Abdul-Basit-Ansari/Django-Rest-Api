# Generated by Django 3.2.8 on 2022-06-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students_Marks',
            fields=[
                ('roll_number', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=40)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]