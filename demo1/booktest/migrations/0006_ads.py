# Generated by Django 2.2.1 on 2019-07-08 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_application_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=10)),
                ('img', models.ImageField(upload_to='ads')),
            ],
        ),
    ]
