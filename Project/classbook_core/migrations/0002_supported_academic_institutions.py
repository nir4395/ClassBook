from django.db import migrations, transaction
from classbook_core.models import Institution


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0001_initial'),
    ]

    def generate_supported_institutions_data(apps, schema_editor):
        supported_institutions = [
          
          # institution_name, student_count, academic_email_suffix
            ('Academic College of TLV',         0, '@mta.ac.il'),
            ('TLV University',                  0, '@mail.tau.ac.il'),
            ('Technion',                        0, '@cs.technion.ac.il'),
            ('University Of Haifa',             0, '@haifa.ac.il'),
            ('Bar Ilan University',             0, '@biu.ac.il'),
            ('Ariel University',                0, '@ariel.ac.il'),
            ('Hebrew University of Jerusalem',  0, '@mail.huji.ac.il'),
            ('IDC Herzelia',                    0, '@idc.ac.il'),
            ('Afeka College',                   0, '@afeka.ac.il'),
            ('HIT',                             0, '@hit.ac.il'),
            ('Shenkar College',                 0, '@shenkar.ac.il'),
            ('Sami Shamoon College',            0, '@sce.ac.il'),
        ]

        with transaction.atomic():
            for institution_name, student_count, academic_email_suffix in supported_institutions:
                Institution(name=institution_name, student_count=student_count, academic_email_suffix=academic_email_suffix).save()

                
    operations = [
        migrations.RunPython(generate_supported_institutions_data),
    ]