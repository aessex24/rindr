# Generated by Django 3.2.8 on 2021-10-30 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20211030_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='opened',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='responded',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='updated',
        ),
    ]
