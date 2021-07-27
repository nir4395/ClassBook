from django.db import migrations, transaction
from classbook_core.models import Institution


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0004_builtin_superuser'),
    ]

    def generate_supported_institutions_data(apps, schema_editor):
        supported_institutions = [
          
          # institution_id, institution_name, student_count, accademic_email_suffix
            (0, 'Academic College of TLV', 0, '@mail.tau.ac.il'),
            (1, 'TLV University', 0, '@mail.tau.ac.il'),
            (2, 'Technion', 0, '@mail.tau.ac.il'),
            (3, 'University Of Haifa', 0, '@mail.tau.ac.il'),
            (4, 'Bar Ilan University', 0, '@mail.tau.ac.il'),
            (5, 'Ariel University', 0, '@mail.tau.ac.il'),
            (6, 'Hebrew University of Jersulam', 0, '@mail.tau.ac.il'),
            (7, 'IDC Harezlia', 0, '@mail.tau.ac.il'),
            (8, 'Afeka College ', 0, '@mail.tau.ac.il'),
            (9, 'HIT', 0, '@mail.tau.ac.il'),
            (10, 'Shenkar College', 0, '@mail.tau.ac.il'),
            (11, 'Sami Shamoon College', 0, '@mail.tau.ac.il'),
        ]

        with transaction.atomic():
            for institution_id, institution_name, student_count, accademic_email_suffix in supported_institutions:
                institution = Institution(institution_id=institution_id, name=institution_name, student_count=student_count, accademic_email_suffix=accademic_email_suffix).save()

                
    operations = [
        migrations.RunPython(generate_supported_institutions_data),
    ]