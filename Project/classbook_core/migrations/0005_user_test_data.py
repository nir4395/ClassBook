from django.db import migrations, transaction
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0004_builtin_superuser')
    ]

    def generate_user_test_data(apps, schema_editor):
        users_test_data = [
            # save all usersnames in lower case - important (we ovveride django behaviour that is case sensitive by using only lower case usernames)
            ("Leon", "Rabinovich", "leon123", "Leon@mta.ac.il", "Password1"),
            ("Guy", "Ronen", "guyno1", "guy_r@mta.ac.il", "password123"),
            ("Boaz", "Cohen", "boaz77", "boaz@mta.ac.il", "password123"),
            ("Elinor", "Lutzski", "el4hjsda", "ellanor@mta.ac.il", "User4Password"),
        ]

        with transaction.atomic():
            for fname, lname, user_name, user_email, user_password in users_test_data:
                User.objects.create_user(user_name, user_email, user_password, first_name=fname, last_name=lname)

    operations = [
        migrations.RunPython(generate_user_test_data),
    ]