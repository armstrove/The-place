# Generated by Django 2.1.1 on 2019-02-14 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languageTests', '0002_languagetest_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languagetest',
            name='excersise',
        ),
        migrations.AddField(
            model_name='excersise',
            name='language_test',
            field=models.ForeignKey(help_text='Unique test', null=True, on_delete=django.db.models.deletion.SET_NULL, to='languageTests.LanguageTest'),
        ),
    ]
