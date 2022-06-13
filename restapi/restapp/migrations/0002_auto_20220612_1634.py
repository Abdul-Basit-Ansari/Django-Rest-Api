# Generated by Django 3.2.8 on 2022-06-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Students_Marks',
        ),
    ]
