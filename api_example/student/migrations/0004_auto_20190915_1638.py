# Generated by Django 2.2.5 on 2019-09-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190915_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.RemoveField(
            model_name='student',
            name='registrations',
        ),
        migrations.AddField(
            model_name='student',
            name='Courses',
            field=models.ManyToManyField(to='student.Course'),
        ),
    ]
