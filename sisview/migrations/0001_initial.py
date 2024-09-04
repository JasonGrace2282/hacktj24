# Generated by Django 5.0.3 on 2024-03-05 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='sisview.account')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.FloatField()),
                ('points_possible', models.FloatField()),
                ('percent', models.FloatField()),
                ('name', models.TextField(default='Cumulative')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weights', to='sisview.subject')),
            ],
        ),
    ]
