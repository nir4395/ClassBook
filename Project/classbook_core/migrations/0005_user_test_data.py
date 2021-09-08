from django.db import migrations, transaction
from django.contrib.auth.models import User
from classbook_core.models import Profile, Institution


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
            ("Maya", "Shabtay", "maya", "maya@mta.ac.il", "password3"),
            ("Ziv", "Kramer", "zivkr", "zvk@mta.ac.il", "password567"),
            ("Elinor", "Lutzski", "el4hjsda", "ellanor@mta.ac.il", "password054"),
            ("Israel", "Katz", "israelkatz", "isrkatz@mta.ac.il", "pass1234"),
        ]

        with transaction.atomic():
            for fname, lname, user_name, user_email, user_password in users_test_data:
                User.objects.create_user(user_name, user_email, user_password, first_name=fname, last_name=lname)

            mta = Institution.objects.get(pk=1)
            for profile in Profile.objects.filter():
                profile.institution = mta
                profile.save()
                

    operations = [
        migrations.RunPython(generate_user_test_data),
    ]