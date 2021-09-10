from django.db import migrations, transaction
from classbook_core.models import AcademicDegree, Institution
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0001_initial'),
        ('classbook_core', '0002_supported_academic_institutions'),
    ]

    def generate_mta_test_data(apps, schema_editor):
        
        MTA_INSTITUTION = Institution.objects.get(name='Academic College of TLV')

        test_data_academic_degree = [
            (MTA_INSTITUTION, 'Computer Science', 3),
            (MTA_INSTITUTION, 'Behavioral Science', 3),
            (MTA_INSTITUTION, 'Psychology', 4),
        ]

        
        with transaction.atomic():
            for institution_id, degree_name, year_count in test_data_academic_degree:
                AcademicDegree(institution=institution_id, name=degree_name, year_count=year_count).save()

    operations = [
        migrations.RunPython(generate_mta_test_data),
    ]