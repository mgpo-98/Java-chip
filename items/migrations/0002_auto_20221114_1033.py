# Generated by Django 3.2.13 on 2022-11-14 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutthiscoffee',
            old_name='content1',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='aboutthiscoffee',
            old_name='content2',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='factsheet',
            old_name='farms',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='factsheet',
            old_name='kind',
            new_name='fieldname',
        ),
        migrations.RemoveField(
            model_name='aboutthiscoffee',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='aboutthiscoffee',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='factsheet',
            name='processed',
        ),
        migrations.RemoveField(
            model_name='factsheet',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='factsheet',
            name='region',
        ),
        migrations.RemoveField(
            model_name='factsheet',
            name='roasting',
        ),
        migrations.RemoveField(
            model_name='itemdetail',
            name='image',
        ),
        migrations.RemoveField(
            model_name='itemdetail',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='itemdetail',
            name='story',
        ),
        migrations.RemoveField(
            model_name='itemdetail',
            name='subscribe',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]