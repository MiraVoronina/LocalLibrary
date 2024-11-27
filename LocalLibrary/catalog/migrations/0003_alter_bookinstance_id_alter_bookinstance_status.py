# Generated by Django 5.1.2 on 2024-11-22 17:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_author_date_of_death_alter_book_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='BookInstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='BookInstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1),
        ),
    ]