from django.db import migrations, transaction
from classbook_core.models import Document


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0006_course_test_data'),
    ]

    def generate_course_test_data(apps, schema_editor):

        document_test_data = [
            (1, "2018_AA", "PDF", 3, 1, 'Exam Solutions'), # Intro to CS
            (2, "Homework_3", "PDF", 2, 2, 'Homework'), # Calculus 1
            (3, "Homework_5", "PDF", 1, 2, 'Homework'), # Calculus 1
            (4, "Sikum_2011", "PDF", 4, 3, 'Summary'), # Linear Algebra One
            (5, "2021_BA", "PDF", 4, 4, 'Exams'), # Algorithms
            (6, "Class_example_1", "cs", 1, 6, 'MISC'), # C# and .NET Framework
        ]

        documents = [Document(*tdc) for tdc in document_test_data]

        with transaction.atomic():
            for doc in documents:
                doc.save()

    operations = [
        migrations.RunPython(generate_course_test_data),
    ]