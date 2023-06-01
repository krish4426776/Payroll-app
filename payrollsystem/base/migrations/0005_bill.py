# Generated by Django 4.2.1 on 2023-05-23 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_utype_customuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.BooleanField(choices=[('False', 'FULFILLED'), ('True', 'UNFULFILLED')], default=False)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.buyer')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.seller')),
            ],
        ),
    ]
