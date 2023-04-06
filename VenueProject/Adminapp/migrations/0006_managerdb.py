# Generated by Django 3.2.16 on 2023-03-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0005_delete_managerdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='managerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('venuename', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=12)),
                ('image', models.ImageField(upload_to='Manager')),
            ],
        ),
    ]
