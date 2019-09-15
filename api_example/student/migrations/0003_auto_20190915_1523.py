# Generated by Django 2.2.5 on 2019-09-15 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190915_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=50)),
                ('Code', models.IntegerField()),
                ('Professor', models.CharField(max_length=50)),
                ('Capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('CourseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Course')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='registrations',
            field=models.ManyToManyField(to='student.CourseRegistration'),
        ),
    ]