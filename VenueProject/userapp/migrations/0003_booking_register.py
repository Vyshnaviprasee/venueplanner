# Generated by Django 3.2.16 on 2023-03-30 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Adminapp', '0005_delete_managerdb'),
        ('userapp', '0002_delete_registerdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_service', models.CharField(max_length=20)),
                ('date_time', models.DateTimeField()),
                ('purpose', models.CharField(max_length=20)),
                ('service_amount', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.register')),
                ('venueid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.venuedb')),
            ],
        ),
    ]