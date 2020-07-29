# Generated by Django 2.2.14 on 2020-07-29 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(default='', max_length=64)),
                ('tracked', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
        migrations.CreateModel(
            name='Mainwhell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(default='', max_length=64)),
                ('tracked', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
    ]
