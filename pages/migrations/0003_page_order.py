# Generated by Django 4.2 on 2023-04-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_created_at_alter_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Orden'),
        ),
    ]
