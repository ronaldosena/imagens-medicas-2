# Generated by Django 2.2.6 on 2019-11-13 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('im2webapp', '0011_auto_20191113_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filterimagemodifier',
            old_name='argument1_name',
            new_name='filter_argument_name',
        ),
        migrations.RenameField(
            model_name='filterimagemodifier',
            old_name='argument1_value',
            new_name='filter_argument_value',
        ),
    ]
