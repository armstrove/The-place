# Generated by Django 2.1.1 on 2020-03-26 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languageTests', '0003_auto_20200324_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='excersise',
            field=models.ForeignKey(help_text='Answer of excersise', null=True, on_delete=django.db.models.deletion.CASCADE, to='languageTests.Excersise'),
        ),
        migrations.AlterField(
            model_name='excersise',
            name='language_test',
            field=models.ForeignKey(help_text='Unique test', null=True, on_delete=django.db.models.deletion.CASCADE, to='languageTests.LanguageTest'),
        ),
        migrations.AlterField(
            model_name='explanation',
            name='answer',
            field=models.ForeignKey(help_text='Explanation of the answer', null=True, on_delete=django.db.models.deletion.CASCADE, to='languageTests.Answer'),
        ),
        migrations.AlterField(
            model_name='tutorialcomponent',
            name='tutorial',
            field=models.ForeignKey(blank=True, help_text='Tutorial', null=True, on_delete=django.db.models.deletion.CASCADE, to='languageTests.Tutorial'),
        ),
    ]