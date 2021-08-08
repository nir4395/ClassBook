# Generated by Django 3.2.5 on 2021-08-03 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0007_document_test_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_authors', to='classbook_core.profile'),
        ),
    ]
