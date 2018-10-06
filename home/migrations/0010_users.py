# Generated by Django 2.1 on 2018-09-30 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], max_length=10)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('Mech', 'Mech'), ('Bio Tech', 'Bio Tech')], max_length=100)),
                ('github_handle', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
