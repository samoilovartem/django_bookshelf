# Generated by Django 4.1 on 2022-08-07 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
