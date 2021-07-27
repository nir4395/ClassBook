from django.db import migrations, transaction
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0004_builtin_superuser')
    ]

    def generate_user_test_data(apps, schema_editor):
        users_test_data = [
            ('Guy', 'Ronen', 'guyno1', 'guy_r@mta.ac.il', 'password123'),
            ('Boaz', 'Cohen', 'boaz77', 'boaz@mta.ac.il', 'Password456'),
            ('Daniel', 'Levi', 'dl1' 'daniell2@mta.ac.il', 'User3Password'),
            ('Elinor', 'Lutzki ', 'EL4', 'ellanor@mta.ac.il', 'User2Password'),
        ]

        with transaction.atomic():
            for fname, lname, user_name, user_email, user_password in users_test_data:
                user = User.objects.create_user(first_name=fname, last_name=lname, username=user_name, email=user_email, password=user_password)

    operations = [
        migrations.RunPython(generate_user_test_data),
    ]