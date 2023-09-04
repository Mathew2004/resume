# Generated by Django 4.2.4 on 2023-09-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_about_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('des', models.TextField()),
                ('skills', models.CharField(max_length=200)),
                ('pimg1', models.ImageField(upload_to='static/img/projects')),
                ('pimg2', models.ImageField(upload_to='static/img/projects')),
                ('pimg3', models.ImageField(upload_to='static/img/projects')),
                ('live', models.CharField(max_length=300)),
                ('code', models.CharField(max_length=300)),
            ],
        ),
    ]