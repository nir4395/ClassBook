from django.db import migrations, transaction
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.management import create_permissions

class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0008_comments_test_data'),
    ]

    def generate_supported_institutions_data(apps, schema_editor):
        basic_user_groups = [
          
          # Group name, group permissions
            ('Institution Admins', 
            ['add_course',
             'view_course',
             'delete_course',
             'change_course',
             'add_document',
             'view_document',
             'delete_document']),
        ]

        with transaction.atomic():
            for app_config in apps.get_app_configs():
                app_config.models_module = True
                create_permissions(app_config, apps=apps, verbosity=0)
                app_config.models_module = None

            for (current_group, assigned_permissions) in basic_user_groups:
                    
                new_group = Group(name=current_group)
                new_group.save()
                for permission in assigned_permissions:
                    retrieve_permission = Permission.objects.get(codename=permission)
                    new_group.permissions.add(retrieve_permission)

                
    operations = [
        migrations.RunPython(generate_supported_institutions_data),
    ]