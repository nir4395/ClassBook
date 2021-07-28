from django.db import migrations, transaction
from classbook_core.models import Course, Year_Code


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0005_user_test_data'),
    ]

    def generate_course_test_data(apps, schema_editor):

        MTA_id = 1
        CS_degree_id = 1

        course_test_data = [
            (1, "Introduction to CS", MTA_id, CS_degree_id, Year_Code.FIRST),
            (2, "Calculus 1", MTA_id, CS_degree_id, Year_Code.FIRST),
            (3, "Linear Algebra 2", MTA_id, CS_degree_id, Year_Code.SECOND),
            (4, "Algorithms", MTA_id, CS_degree_id, Year_Code.SECOND),
            (5, "Operating Systems", MTA_id, CS_degree_id, Year_Code.THIRD),
            (6, "C# and .NET Programming", MTA_id, CS_degree_id, Year_Code.OPTIONAL),
            (7, "Ethics, Technology and Law", MTA_id, CS_degree_id, Year_Code.OPTIONAL),

        ]

        courses = [Course(*tdc) for tdc in course_test_data]

        with transaction.atomic():
            for c in courses:
                c.save()

    operations = [
        migrations.RunPython(generate_course_test_data),
    ]