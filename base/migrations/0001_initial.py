# Generated by Django 5.1.5 on 2025-01-26 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('main_head', models.TextField()),
                ('inner_title', models.TextField()),
                ('background', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='InnerLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('inner_note', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.service')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('content_2', models.TextField(blank=True, null=True)),
                ('content_3', models.TextField(blank=True, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.service')),
            ],
        ),
    ]
