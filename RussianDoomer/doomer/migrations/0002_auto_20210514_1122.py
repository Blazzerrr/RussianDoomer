# Generated by Django 3.1.7 on 2021-05-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doomer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='datetime',
            field=models.CharField(default='14.05.2021 11:22:54', max_length=64),
        ),
    ]
