# Generated by Django 3.0.4 on 2022-04-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleCrudApp', '0004_auto_20220408_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createuser',
            name='last_name',
            field=models.CharField(max_length=122),
        ),
    ]
