# Generated by Django 2.1.1 on 2019-02-08 12:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excersise',
            fields=[
                ('level', models.CharField(blank=True, choices=[('b', 'Beginner'), ('i', 'Intermediate'), ('e', 'Expert')], default='b', help_text='Excersise level', max_length=1)),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular excersise', primary_key=True, serialize=False)),
                ('text', models.TextField(default='', help_text='Text of the excersise', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the language (e.g. English, French, Japanese etc.)', max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LanguageTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a Test Name (e.g. Test #1)', max_length=200)),
                ('excersise', models.ManyToManyField(help_text='Select excersises for current Test', to='languageTests.Excersise')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='languageTests.Language')),
            ],
        ),
    ]
