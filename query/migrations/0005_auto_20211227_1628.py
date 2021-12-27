# Generated by Django 3.2.8 on 2021-12-27 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0004_auto_20211227_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='select',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.ForeignKey(default='No answer', on_delete=django.db.models.deletion.CASCADE, to='query.answer'),
        ),
    ]
