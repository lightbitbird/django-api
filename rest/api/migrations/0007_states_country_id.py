# Generated by Django 3.0.1 on 2020-01-04 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200104_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='states',
            name='country_id',
            field=models.IntegerField(null=True),
        ),
    ]
