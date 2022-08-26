# Generated by Django 3.2.5 on 2021-07-25 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_upload_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_as',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='upload_assignment')),
            ],
        ),
        migrations.DeleteModel(
            name='upload_assignment',
        ),
    ]
