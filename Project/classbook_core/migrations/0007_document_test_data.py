from django.db import migrations, transaction
from classbook_core.models import Document, Profile, Course
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0006_course_test_data'),
    ]

    def generate_course_test_data(apps, schema_editor):

        user_example_1 = Profile.objects.get(user=User.objects.get(username='leon123'))
        user_example_2 = Profile.objects.get(user=User.objects.get(username='boaz77'))
        user_example_3 = Profile.objects.get(user=User.objects.get(username='el4hjsda'))
        user_example_4 = Profile.objects.get(user=User.objects.get(username='maya'))

        course_into_to_cs = Course.objects.get(name='Introduction to CS')
        course_calculus1 = Course.objects.get(name='Calculus 1')
        course_linear_algebra2 = Course.objects.get(name='Linear Algebra 2')
        course_algorithms = Course.objects.get(name='Algorithms')
        course_operating_systems = Course.objects.get(name='Operating Systems')
        course_complexity = Course.objects.get(name='Complexity')
        course_csharp_dotnet = Course.objects.get(name='C# and .NET Programming')
        course_ethics = Course.objects.get(name='Ethics, Technology and Law')
        course_functional_programming = Course.objects.get(name='Functional Programming')

        document_test_data = [
            ("hw4q1",         "cpp",    user_example_1, course_into_to_cs,       'Homework Solutions'),
            ("hw4q2",         "cpp",    user_example_3, course_into_to_cs,       'Homework Solutions'),
            ("WhatIsCS_Slide",         "PDF",    user_example_4, course_into_to_cs,       'Slides'),
            ("חדוא 1 - תרגיל 5",         "PDF",    user_example_2, course_calculus1,       'Homework Solutions'),
            ("2015.06.26",         "PDF",    user_example_2, course_linear_algebra2,       'Exam Solutions'),
            ("Summary",         "PDF",    user_example_2, course_linear_algebra2,       'Summary'),
            ("recorded_lectures_iris",         "docx",    user_example_1, course_algorithms,       'Lectures'),
            ("targ02-published-sol",         "PDF",    user_example_4, course_algorithms,       'Homework Solutions'),
            ("2016.06.21",         "PDF",    user_example_3, course_operating_systems,       'Exam Solutions'),
            ("BinPacking_misc", "PDF", user_example_1, course_complexity, 'Exam Solutions'),
            ("File System Implementation",         "ppt",    user_example_2, course_operating_systems,       'Slides'),
            ("Targil6",         "PDF",    user_example_3, course_complexity,       'Homework Solutions'),
            ("HelloWorld",         "cs",    user_example_1, course_csharp_dotnet,       'Homework Solutions'),
            ("חוק המחשבים",         "PDF",    user_example_4, course_ethics,       'MISC'),
            ("Haskell Notes",         "DOCX",    user_example_4, course_functional_programming,       'Summary'),
        ]

        with transaction.atomic():
            for name, doc_type, author, course, category, in document_test_data:
                Document(name=name, doc_type=doc_type, author=author, course=course, category=category).save()

    operations = [
        migrations.RunPython(generate_course_test_data),
    ]