# Generated by Django 3.0.8 on 2022-01-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeMessages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('cdate', models.DateField()),
                ('ctime', models.TimeField()),
                ('docfile', models.FileField(upload_to='')),
            ],
        ),
    ]