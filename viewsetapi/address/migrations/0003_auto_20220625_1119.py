# Generated by Django 3.0.2 on 2022-06-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20220624_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='phone_name',
        ),
        migrations.AddField(
            model_name='parent',
            name='phone_num',
            field=models.CharField(default='Individual', max_length=100),
        ),
    ]
