# Generated by Django 3.1.7 on 2021-05-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doomer', '0002_auto_20210514_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='datetime',
            field=models.CharField(default='14.05.2021 11:23:11', max_length=64),
        ),
    ]