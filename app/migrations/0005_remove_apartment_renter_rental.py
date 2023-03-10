# Generated by Django 4.1.7 on 2023-03-07 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_renter_remove_apartment_user_apartment_renter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='renter',
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.apartment')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.renter')),
            ],
        ),
    ]
