# Generated by Django 3.2.8 on 2021-12-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0015_merge_0011_auto_20211208_1409_0014_auto_20211115_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='delta',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='lapse',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='difficulty',
            field=models.CharField(choices=[('1', '1  - Simplest (Did you RTFM?)'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6 - Bloody hard. (My name is Neo.)')], default='2', max_length=2, verbose_name='Ticket Debug Difficulty'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='system',
            field=models.CharField(choices=[('o', 'ODINs'), ('b', 'BlueJays'), ('m', 'Mattermost'), ('k', 'BuildKite')], default='o', max_length=2, verbose_name='Ticket originated in System'),
        ),
    ]