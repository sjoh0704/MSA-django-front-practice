# Generated by Django 3.1.7 on 2021-05-19 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20210518_0044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set(),
        ),
        migrations.DeleteModel(
            name='FollowRelation',
        ),
    ]