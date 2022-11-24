# Generated by Django 4.1.3 on 2022-11-24 05:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('answer', models.CharField(max_length=10)),
                ('result', models.CharField(max_length=10)),
                ('is_answer_check', models.BooleanField(max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
