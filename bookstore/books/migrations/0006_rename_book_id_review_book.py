# Generated by Django 4.1 on 2022-08-07 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_review_book_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='book_id',
            new_name='book',
        ),
    ]
