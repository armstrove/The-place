# Generated by Django 2.1.1 on 2020-03-07 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('languageTests', '0009_languagetest_exercise_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.CharField(help_text='Enter a Tutorial Name (e.g. Present simple #1)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TutorialComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_type', models.CharField(blank=True, choices=[('e', 'Explanation'), ('p', 'Picture'), ('c', 'Chart'), ('x', 'Example')], default='e', help_text='Component type', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='languagetest',
            name='exercise_type',
        ),
        migrations.AddField(
            model_name='excersise',
            name='exercise_type',
            field=models.CharField(blank=True, choices=[('w', 'Place words'), ('s', 'Construct a sentance')], default='w', help_text='Tests type', max_length=1),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_component',
            field=models.ForeignKey(help_text='Tutorial Component', null=True, on_delete=django.db.models.deletion.SET_NULL, to='languageTests.TutorialComponent'),
        ),
    ]
