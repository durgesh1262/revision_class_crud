# Generated by Django 4.1.3 on 2022-11-28 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='emali',
            new_name='email',
        ),
    ]
