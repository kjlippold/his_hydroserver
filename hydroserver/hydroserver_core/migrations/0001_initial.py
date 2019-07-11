# Generated by Django 2.1.7 on 2019-07-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('network_id', models.TextField()),
                ('database_id', models.TextField()),
                ('database_name', models.TextField(default='None')),
                ('database_path', models.TextField(default='None')),
                ('database_type', models.TextField(default='None')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('network_id', models.TextField(unique=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Timeseries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('site_name', models.TextField()),
                ('site_code', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('variable_name', models.TextField()),
                ('variable_code', models.TextField()),
                ('sample_medium', models.TextField()),
                ('value_count', models.IntegerField()),
                ('begin_date', models.TextField()),
                ('end_date', models.TextField()),
                ('method_link', models.TextField()),
                ('method_description', models.TextField()),
                ('network_id', models.TextField()),
                ('database_id', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='timeseries',
            unique_together={('network_id', 'database_id', 'site_code', 'variable_code')},
        ),
        migrations.AlterUniqueTogether(
            name='database',
            unique_together={('network_id', 'database_id')},
        ),
    ]
