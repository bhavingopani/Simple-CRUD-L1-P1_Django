# Generated by Django 3.0.4 on 2022-04-08 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleCrudApp', '0002_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createuser',
            name='email',
            field=models.CharField(max_length=122, unique=True),
        ),
    ]
