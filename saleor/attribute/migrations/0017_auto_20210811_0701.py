# Generated by Django 3.2.5 on 2021-08-11 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attribute", "0016_auto_20210827_0938"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attribute",
            name="input_type",
            field=models.CharField(
                choices=[
                    ("dropdown", "Dropdown"),
                    ("multiselect", "Multi Select"),
                    ("file", "File"),
                    ("reference", "Reference"),
                    ("numeric", "Numeric"),
                    ("rich-text", "Rich Text"),
                    ("swatch", "Swatch"),
                    ("boolean", "Boolean"),
                    ("date", "Date"),
                    ("date-time", "Date Time"),
                ],
                default="dropdown",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="attributevalue",
            name="value",
            field=models.CharField(blank=True, default="", max_length=9),
        ),
    ]