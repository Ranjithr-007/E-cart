# Generated by Django 3.1.7 on 2021-04-21 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0003_coupons'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='live',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coupons',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
