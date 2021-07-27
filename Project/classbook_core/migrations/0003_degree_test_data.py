from django.db import migrations, transaction
from classbook_core.models import AcademicDegree
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0001_initial'),
        ('classbook_core', '0002_ins_test_data'),
    ]

    def generate_mta_test_data(apps, schema_editor):
        
        MTA_id = 1

        test_data_academic_degree = [
            (1, MTA_id, 'Computer Science'),
            (2, MTA_id, 'Behavioral Science'),
            (3, MTA_id, 'Psychology'),
        ]

        academic_degrees = [AcademicDegree(*tdc) for tdc in test_data_academic_degree]

        with transaction.atomic():
            for degree in academic_degrees:
                degree.save()

    operations = [
        migrations.RunPython(generate_mta_test_data),
    ]