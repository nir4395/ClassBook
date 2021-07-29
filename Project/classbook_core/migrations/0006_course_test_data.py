from classbook_core.models import AcademicDegree
from django.db import migrations, transaction
from classbook_core.models import Course, Year_Code, Institution


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0005_user_test_data'),
    ]

    def generate_course_test_data(apps, schema_editor):

        MTA_INSTITUTION = Institution.objects.get(name='Academic College of TLV')
        COMPUTERSIENCE_DEGREE = AcademicDegree.objects.get(name='Computer Science')

        course_test_data = [
            ("Introduction to CS", MTA_INSTITUTION, COMPUTERSIENCE_DEGREE, Year_Code.FIRST),
            ("Calculus 1", MTA_INSTITUTION, COMPUTERSIENCE_DEGREE, Year_Code.FIRST),
            ("Linear Algebra 2", MTA_INSTITUTION, COMPUTERSIENCE_DEGREE, Year_Code.SECOND),
            ("Algorithms", MTA_INSTITUTION, COMPUTERSIENCE_DEGREE, Year_Code.SECOND),
            ("Operating Systems", MTA_INSTITUTION, COMPUTERSIENCE_DEGREE, Year_Code.THIRD),
            ("C# and .NET Programming", MTA_INSTITUTION, COMPUTERSIENCE_DEGREE, Year_Code.OPTIONAL),
            ("Ethics, Technology and Law", MTA_INSTITUTION, COMPUTERSIENCE_DEGREE, Year_Code.OPTIONAL),

        ]

        with transaction.atomic():
            for name, institution, degree, year_code in course_test_data:
                Course(name=name, institution=institution, degree=degree, year_code=year_code).save()

    operations = [
        migrations.RunPython(generate_course_test_data),
    ]