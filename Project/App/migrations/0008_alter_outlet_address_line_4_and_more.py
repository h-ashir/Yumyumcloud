# Generated by Django 5.0.2 on 2024-02-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_outlet_outlet_landline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlet',
            name='address_line_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='outlet',
            name='address_line_5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
