# Generated by Django 5.0.6 on 2024-06-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_platform', '0003_alter_network_options_network_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='name',
            field=models.CharField(max_length=150, verbose_name='название'),
        ),
    ]
