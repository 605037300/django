# Generated by Django 2.2.14 on 2020-07-29 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(default='', max_length=64)),
                ('tracked', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('main_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app01.Main')),
            ],
            options={
                'db_table': 'axf_nav',
            },
            bases=('app01.main',),
        ),
        migrations.CreateModel(
            name='Mainwhell',
            fields=[
                ('main_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app01.Main')),
            ],
            options={
                'db_table': 'axf_wheel',
            },
            bases=('app01.main',),
        ),
    ]
