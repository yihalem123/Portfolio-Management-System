import django.contrib.postgres.fields
from django.db import migrations, models

def set_default_buying_values(apps, schema_editor):
    StockHolding = apps.get_model('dashboard', 'StockHolding')
    for stockholding in StockHolding.objects.all():
        # Modify the default value of the buying_values field
        stockholding.buying_values = [[0.0]]  # Assuming buying_values is a 2D array
        stockholding.save()

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_stockholding_buying_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockholding',
            name='buying_values',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=django.contrib.postgres.fields.ArrayField(
                    base_field=models.FloatField(),  # Remove default value here
                    blank=True,
                ),
                blank=True,
                default=[],  # Default value as empty list
                size=None,
            ),
            preserve_default=False,  # Remove preserve_default=False
        ),
        migrations.RunPython(set_default_buying_values),  # Run function to set default values
    ]
