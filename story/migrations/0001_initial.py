# Generated by Django 2.2 on 2020-09-14 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('des', models.TextField()),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.Category')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
    ]
