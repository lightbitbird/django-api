# Generated by Django 3.0.1 on 2020-01-04 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200101_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('carbohydrate', models.DecimalField(decimal_places=1, max_digits=7)),
                ('protein', models.DecimalField(decimal_places=1, max_digits=7)),
                ('lipid', models.DecimalField(decimal_places=1, max_digits=7)),
                ('vitamin', models.DecimalField(decimal_places=1, max_digits=7)),
                ('calcium', models.DecimalField(decimal_places=1, max_digits=7)),
                ('iron', models.DecimalField(decimal_places=1, max_digits=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('published_at', 'id')},
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='api.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_at',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='FoodStuff',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('nutrients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutrients', to='api.Nutrients')),
            ],
        ),
    ]
