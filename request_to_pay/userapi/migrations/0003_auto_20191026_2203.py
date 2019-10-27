# Generated by Django 2.2.6 on 2019-10-27 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
