# Generated by Django 2.2.5 on 2019-09-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('studentId', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Sutdent',
                'verbose_name_plural': 'Students',
            },
        ),
    ]
