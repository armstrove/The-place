# Generated by Django 2.1.1 on 2020-04-22 20:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('languageTests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished', models.BooleanField(default=False)),
                ('started', models.BooleanField(default=False)),
                ('visited_times', models.IntegerField(default=0)),
                ('failed_times', models.IntegerField(default=0)),
                ('passed_times', models.IntegerField(default=0)),
                ('language_test', models.ForeignKey(on_delete='CASCADE', to='languageTests.LanguageTest')),
                ('user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopicProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished', models.BooleanField(default=False)),
                ('started', models.BooleanField(default=False)),
                ('visited_times', models.IntegerField(default=0)),
                ('topic', models.ForeignKey(on_delete='CASCADE', to='languageTests.Topic')),
                ('user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
