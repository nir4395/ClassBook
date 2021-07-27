from django.db import migrations, transaction
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0003_degree_test_data'),
     ]

    def generate_builtin_superuser(apps, schema_editor):
        with transaction.atomic():
            user = User.objects.create_superuser(
                username='admin', email='builtin_admin@ClassBook.com', password='ClassBook0!')

    operations = [
        migrations.RunPython(generate_builtin_superuser),
    ]