# Generated by Django 4.0.2 on 2022-04-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='CITY',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CNAME',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='STATE',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ZIP',
            field=models.CharField(max_length=10),
        ),
    ]