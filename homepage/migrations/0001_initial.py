# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=30, verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('securtiy_question', models.TextField(blank=True, max_length=150, null=True)),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('address1', models.TextField(blank=True, max_length=30, null=True)),
                ('address2', models.TextField(blank=True, max_length=30, null=True)),
                ('city', models.TextField(blank=True, max_length=30, null=True)),
                ('state', models.TextField(blank=True, max_length=30, null=True)),
                ('country', models.TextField(blank=True, max_length=30, null=True)),
                ('zip', models.TextField(blank=True, max_length=30, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', verbose_name='groups', to='auth.Group', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_query_name='user', verbose_name='user permissions', to='auth.Permission', related_name='user_set')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('account_name', models.TextField(blank=True, max_length=75, null=True)),
                ('amount', models.DecimalField(max_digits=12, blank=True, decimal_places=2, null=True)),
                ('acc_type', models.TextField(max_length=75)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DebCred',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.TextField(blank=True, max_length=75, null=True)),
                ('cost', models.DecimalField(max_digits=12, blank=True, decimal_places=2, null=True)),
                ('tran_type', models.TextField(blank=True, max_length=75, null=True)),
                ('year', models.TextField(blank=True, max_length=75, null=True)),
                ('month', models.TextField(blank=True, max_length=75, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('filepath', models.CharField(max_length=255)),
                ('transaction', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=75, null=True)),
                ('original_description', models.TextField(blank=True, max_length=75, null=True)),
                ('amount', models.DecimalField(max_digits=12, blank=True, decimal_places=2, null=True)),
                ('transaction_type', models.TextField(blank=True, max_length=75, null=True)),
                ('category', models.TextField(blank=True, max_length=75, null=True)),
                ('account_name', models.TextField(blank=True, max_length=75, null=True)),
                ('User', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('account', models.ForeignKey(to='homepage.Account', null=True)),
            ],
        ),
    ]
