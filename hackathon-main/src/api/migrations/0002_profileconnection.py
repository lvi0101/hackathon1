# Generated by Django 2.1.7 on 2019-02-23 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190223_0409'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Connection')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
        ),
    ]
