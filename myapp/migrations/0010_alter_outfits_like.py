# Generated by Django 4.2.6 on 2024-02-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_alter_outfits_like"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outfits", name="like", field=models.BooleanField(default=False),
        ),
    ]
