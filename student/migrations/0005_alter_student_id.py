# Generated by Django 5.1.4 on 2025-01-11 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_delete_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
