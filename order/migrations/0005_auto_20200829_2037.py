# Generated by Django 3.0.8 on 2020-08-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200829_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
