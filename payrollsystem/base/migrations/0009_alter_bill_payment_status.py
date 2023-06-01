# Generated by Django 4.2.1 on 2023-05-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_bill_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='payment_status',
            field=models.CharField(choices=[('fulfilled', 'FULFILLED'), ('unfulfilled', 'UNFULFILLED')], default='unfulfilled', max_length=20),
        ),
    ]
