# Generated by Django 2.1.7 on 2019-06-01 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargePoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slots', models.PositiveIntegerField()),
                ('slots_occupied', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChargerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('others', models.TextField(default='{}')),
            ],
        ),
        migrations.CreateModel(
            name='ChargeStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=50)),
                ('charger_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ev.ChargerType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User2')),
            ],
        ),
        migrations.AddField(
            model_name='chargepoints',
            name='charge_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='ev.ChargeStation'),
        ),
        migrations.AddField(
            model_name='chargepoints',
            name='charger_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='ev.ChargerType'),
        ),
    ]
