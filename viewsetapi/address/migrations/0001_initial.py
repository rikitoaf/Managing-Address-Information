# Generated by Django 2.2 on 2022-06-24 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_name', models.EmailField(max_length=100)),
                ('phone_name', models.IntegerField()),
                ('address_name', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('parent_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.Parent')),
            ],
        ),
    ]