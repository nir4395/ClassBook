from django.db import migrations, transaction
from classbook_core.models import Institution


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0001_initial'),
    ]

    def generate_supported_institutions_data(apps, schema_editor):
        supported_institutions = [
          
          # institution_name, student_count, accademic_email_suffix
            ('Academic College of TLV', 0, '@mail.tau.ac.il'),
            ('TLV University', 0, '@mail.tau.ac.il'),
            ('Technion', 0, '@mail.tau.ac.il'),
            ('University Of Haifa', 0, '@mail.tau.ac.il'),
            ('Bar Ilan University', 0, '@mail.tau.ac.il'),
            ('Ariel University', 0, '@mail.tau.ac.il'),
            ('Hebrew University of Jersulam', 0, '@mail.tau.ac.il'),
            ('IDC Harezlia', 0, '@mail.tau.ac.il'),
            ('Afeka College ', 0, '@mail.tau.ac.il'),
            ('HIT', 0, '@mail.tau.ac.il'),
            ('Shenkar College', 0, '@mail.tau.ac.il'),
            ('Sami Shamoon College', 0, '@mail.tau.ac.il'),
        ]

        with transaction.atomic():
            for institution_name, student_count, accademic_email_suffix in supported_institutions:
                Institution(name=institution_name, student_count=student_count, accademic_email_suffix=accademic_email_suffix).save()

                
    operations = [
        migrations.RunPython(generate_supported_institutions_data),
    ]