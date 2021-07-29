from django.db import migrations, transaction
from classbook_core.models import Document, Profile, Course
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0006_course_test_data'),
    ]

    def generate_course_test_data(apps, schema_editor):

        user_of_profile = User.objects.get(username='leon123')
        document_auther = Profile.objects.get(user=user_of_profile)
        
        course_into_to_cs = Course.objects.get(name='Introduction to CS')
        course_calculus1 = Course.objects.get(name='Calculus 1')
        course_linear_algebra2 = Course.objects.get(name='Linear Algebra 2')
        course_algorithms = Course.objects.get(name='Algorithms')
        course_csharp_dotnet = Course.objects.get(name='C# and .NET Programming')

        document_test_data = [
            ("2018_AA",         "PDF",    document_auther, course_into_to_cs,       'Exam Solutions'),
            ("Homework_3",      "PDF",    document_auther, course_calculus1,        'Homework'),
            ("Homework_5",      "PDF",    document_auther, course_calculus1,        'Homework'),
            ("Sikum_2011",      "PDF",    document_auther, course_linear_algebra2,  'Summary'),
            ("2021_BA",         "PDF",    document_auther, course_algorithms,       'Exams'),
            ("Class_example_1", "PDF",    document_auther, course_csharp_dotnet,    'MISC'),
        ]

        with transaction.atomic():
            for name, doc_type, author, course, category, in document_test_data:
                Document(name=name, doc_type=doc_type, author=author, course=course, category=category).save()

    operations = [
        migrations.RunPython(generate_course_test_data),
    ]