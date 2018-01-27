# Generated by Django 2.0 on 2017-12-30 14:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20171225_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d58e82b2-8041-4cb7-a679-fe82e47d88db'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
