# Generated by Django 2.2.2 on 2019-06-11 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('secretary', 'secretary'), ('instructor', 'instructor'), ('students', 'students')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payed_hour', models.IntegerField(default=0)),
                ('lessons', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driving_school.User')),
            ],
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='driving_school.User')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='driving_school.User')),
            ],
        ),
    ]
