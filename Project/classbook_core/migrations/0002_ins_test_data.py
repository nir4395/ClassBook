from django.db import migrations, transaction
from classbook_core.models import Institution
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0001_initial'),
    ]

    def generate_mta_test_data(apps, schema_editor):
        
        test_data_institution = [
            (1, 'Academic College of Tel-Aviv Yafo', 0),
            (2, 'Ben-Gurion University', 0),
        ]

        institutions = [Institution(*tdc) for tdc in test_data_institution]

        with transaction.atomic():
            for institution in institutions:
                institution.save()

    operations = [
        migrations.RunPython(generate_mta_test_data),
    ]