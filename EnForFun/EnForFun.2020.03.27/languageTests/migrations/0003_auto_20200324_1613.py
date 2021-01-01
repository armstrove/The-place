# Generated by Django 2.1.1 on 2020-03-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languageTests', '0002_auto_20200322_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excersise',
            name='level',
        ),
        migrations.AlterField(
            model_name='excersise',
            name='exercise_type',
            field=models.CharField(blank=True, choices=[('w', 'Choose the word'), ('s', 'Construct a sentance'), ('t', 'Type the word')], default='w', help_text='Tests type', max_length=1),
        ),
    ]