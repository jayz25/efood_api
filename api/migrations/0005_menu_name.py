# Generated by Django 4.2.2 on 2023-07-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_menu_cuisines'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
