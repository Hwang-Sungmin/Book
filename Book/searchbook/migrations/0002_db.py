# Generated by Django 3.0.2 on 2020-02-14 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField()),
                ('kind', models.TextField()),
                ('date', models.TextField()),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('genre', models.TextField()),
            ],
        ),
    ]