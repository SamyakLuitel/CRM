# Generated by Django 3.2.3 on 2021-05-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_order_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
