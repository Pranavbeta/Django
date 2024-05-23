# Generated by Django 5.0.6 on 2024-05-14 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uom_name', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('price_per_unit', models.BigIntegerField()),
                ('uom_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product.uom')),
            ],
        ),
    ]