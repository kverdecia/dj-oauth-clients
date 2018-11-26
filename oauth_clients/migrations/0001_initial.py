# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-21 19:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('token_type', models.CharField(max_length=255, verbose_name='Token type')),
                ('expires_in', models.IntegerField(verbose_name='Expires in')),
                ('access_token', models.CharField(max_length=255, verbose_name='Access token')),
                ('refresh_token', models.CharField(max_length=255, verbose_name='Refresh token')),
            ],
            options={
                'verbose_name': 'Access token',
                'verbose_name_plural': 'Access tokens',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('client_id', models.CharField(max_length=255, unique=True, verbose_name='Client id')),
                ('client_secret', models.CharField(max_length=255, verbose_name='Client secret')),
                ('authorization_endpoint', models.URLField(max_length=255, verbose_name='Authorization endpoint')),
                ('token_endpoint', models.URLField(blank=True, default=b'', max_length=255, verbose_name='Token endpoint')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Oauth2 client',
                'verbose_name_plural': 'Oauth2 clients',
            },
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth_clients.Client', verbose_name='Client'),
        ),
    ]
