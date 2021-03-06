# Generated by Django 2.0.1 on 2018-01-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiveagentSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_id', models.CharField(max_length=255)),
                ('liveagent_id', models.CharField(blank=True, max_length=255, null=True)),
                ('key', models.CharField(blank=True, max_length=255, null=True)),
                ('affinity_token', models.CharField(blank=True, max_length=255, null=True)),
                ('sequence', models.IntegerField(blank=True, null=True)),
                ('ack', models.IntegerField(blank=True, null=True)),
                ('responder', models.CharField(default='LIVEAGENT', max_length=255)),
            ],
            options={
                'db_table': 'liveagent_session',
            },
        ),
    ]
