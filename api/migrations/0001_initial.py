# Generated by Django 4.1.7 on 2023-03-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, default='off', max_length=100, null=True)),
                ('pid', models.SmallIntegerField(default=0)),
                ('first_name', models.CharField(default='None', max_length=100)),
                ('chat_id', models.IntegerField(default=0)),
                ('license_date', models.DateField()),
                ('fruitpass', models.CharField(default='None', max_length=200)),
                ('second', models.IntegerField(default=0)),
            ],
        ),
    ]