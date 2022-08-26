# Generated by Django 3.2.5 on 2021-07-22 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210721_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ass_name', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('pdf', models.FileField(upload_to='pdf_ass')),
            ],
        ),
    ]