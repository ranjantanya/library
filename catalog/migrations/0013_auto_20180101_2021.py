# Generated by Django 2.0 on 2018-01-01 14:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20180101_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5caf143d-dbd9-44ca-8b5b-8d337165605e'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]