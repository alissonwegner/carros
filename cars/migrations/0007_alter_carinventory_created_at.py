# Generated by Django 5.0.1 on 2024-02-25 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_car_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinventory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
