# Generated by Django 2.2.1 on 2019-07-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_account_contract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('h', models.ManyToManyField(to='booktest.Host')),
            ],
        ),
    ]
