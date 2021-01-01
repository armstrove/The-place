# Generated by Django 2.1.1 on 2020-03-21 18:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_string', models.CharField(help_text='Enter the answer', max_length=100)),
                ('possible_answers', models.CharField(help_text='Enter the possible answers', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Excersise',
            fields=[
                ('level', models.CharField(blank=True, choices=[('b', 'Beginner'), ('i', 'Intermediate'), ('e', 'Expert')], default='b', help_text='Excersise level', max_length=1)),
                ('exercise_type', models.CharField(blank=True, choices=[('w', 'Place words'), ('s', 'Construct a sentance')], default='w', help_text='Tests type', max_length=1)),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular excersise', primary_key=True, serialize=False)),
                ('text', models.TextField(default='', help_text='Text of the excersise', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explain_text', models.TextField(default='', help_text='Explanation text for the answer', max_length=1000)),
                ('wrong_answer', models.CharField(help_text='Expected wrong answer', max_length=200, null=True)),
                ('answer', models.ForeignKey(help_text='Explanation of the answer', null=True, on_delete=django.db.models.deletion.SET_NULL, to='languageTests.Answer')),
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
                ('task', models.CharField(default='', max_length=1024, null=True)),
                ('number', models.IntegerField(null=True, unique=True)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='languageTests.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('b', 'Beginner'), ('i', 'Intermediate'), ('e', 'Expert')], default='b', help_text='Tests level', max_length=1)),
                ('title', models.CharField(help_text='Enter a Test Name (e.g. Test #1)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.CharField(help_text='Enter a Tutorial Name (e.g. Present simple #1)', max_length=200)),
                ('level', models.CharField(blank=True, choices=[('b', 'Beginner'), ('i', 'Intermediate'), ('e', 'Expert')], default='b', help_text='Tutorial level', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='TutorialComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_type', models.CharField(blank=True, choices=[('e', 'Explanation'), ('p', 'Picture'), ('c', 'Chart'), ('x', 'Example')], default='e', help_text='Component type', max_length=1)),
                ('component_text', models.TextField(blank=True, default='', help_text='Explanation text', max_length=10000)),
                ('tutorial', models.ForeignKey(blank=True, help_text='Tutorial', null=True, on_delete=django.db.models.deletion.SET_NULL, to='languageTests.Tutorial')),
            ],
        ),
        migrations.AddField(
            model_name='languagetest',
            name='language_test_group',
            field=models.ForeignKey(help_text='Unique test', null=True, on_delete=django.db.models.deletion.SET_NULL, to='languageTests.Topic'),
        ),
        migrations.AddField(
            model_name='explanation',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='languageTests.Language'),
        ),
        migrations.AddField(
            model_name='excersise',
            name='language_test',
            field=models.ForeignKey(help_text='Unique test', null=True, on_delete=django.db.models.deletion.SET_NULL, to='languageTests.LanguageTest'),
        ),
        migrations.AddField(
            model_name='answer',
            name='excersise',
            field=models.ForeignKey(help_text='Answer of excersise', null=True, on_delete=django.db.models.deletion.SET_NULL, to='languageTests.Excersise'),
        ),
    ]
