# Generated by Django 2.2.6 on 2022-07-11 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='moddo_preparo',
            new_name='modo_preparo',
        ),
    ]