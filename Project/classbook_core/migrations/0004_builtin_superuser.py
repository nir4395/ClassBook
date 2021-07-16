from django.db import migrations, transaction
from classbook_core.models import AppUser
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0001_initial'),
        ('classbook_core', '0002_ins_test_data'),
        ('classbook_core', '0003_user_test_data'),
     ]

    def generate_builtin_superuser(apps, schema_editor):
        with transaction.atomic():
            user = User.objects.create_superuser(
                username='admin', email='builtin_admin@ClassBook.com', password='ClassBook0!')

            AppUser(user=user).save()

    operations = [
        migrations.RunPython(generate_builtin_superuser),
    ]