# Generated by Django 5.1.5 on 2025-01-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='inner_title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
