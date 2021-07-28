from django.db import migrations, transaction
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0002_supported_accademic_institutions'),
    ]

    def generate_user_test_data(apps, schema_editor):
        users_test_data = [
            ('testUser1', 'user1@gmail.com', 'password123'),
            ('testUser2', 'David@gmail.com', 'Password456'),
            ('testUser3', 'User3@gmail.com', 'User3Password')
        ]

        with transaction.atomic():
            for user_name, user_email, user_password in users_test_data:
                user = User.objects.create_user(username=user_name, email=user_email, password=user_password)

    operations = [
        migrations.RunPython(generate_user_test_data),
    ]