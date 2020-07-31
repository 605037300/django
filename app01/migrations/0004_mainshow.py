# Generated by Django 2.2.14 on 2020-07-30 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_mainshop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('main_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app01.Main')),
                ('categoryid', models.IntegerField(default=1)),
                ('brandname', models.CharField(max_length=64)),
                ('img1', models.CharField(max_length=255)),
                ('childcid1', models.IntegerField(default=1)),
                ('productid1', models.IntegerField(default=1)),
                ('longname1', models.CharField(max_length=128)),
                ('price1', models.FloatField(default=1)),
                ('marketprice1', models.FloatField(default=0)),
                ('img2', models.CharField(max_length=255)),
                ('childcid2', models.IntegerField(default=1)),
                ('productid2', models.IntegerField(default=1)),
                ('longname2', models.CharField(max_length=128)),
                ('price2', models.FloatField(default=1)),
                ('marketprice2', models.FloatField(default=0)),
                ('img3', models.CharField(max_length=255)),
                ('childcid3', models.IntegerField(default=1)),
                ('productid3', models.IntegerField(default=1)),
                ('longname3', models.CharField(max_length=128)),
                ('price3', models.FloatField(default=1)),
                ('marketprice3', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
            bases=('app01.main',),
        ),
    ]
