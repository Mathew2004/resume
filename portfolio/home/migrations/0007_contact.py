# Generated by Django 4.2.4 on 2023-09-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_project_live'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=100)),
                ('msg', models.TextField()),
            ],
        ),
    ]
