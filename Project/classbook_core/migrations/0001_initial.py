# Generated by Django 3.2.5 on 2021-07-29 08:02

import classbook_core.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('year_code', models.SmallIntegerField(default=-2, verbose_name=classbook_core.models.Year_Code)),
                ('student_count', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.academicdegree')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('student_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('accademic_email_suffix', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('institution', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classbook_core.institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('doc_type', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=300)),
                ('view_count', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('rating', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_authers', to='classbook_core.profile')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.course')),
                ('student_rated', models.ManyToManyField(related_name='document_students_rated', to='classbook_core.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.institution'),
        ),
        migrations.AddField(
            model_name='course',
            name='student_enrolled',
            field=models.ManyToManyField(to='classbook_core.Profile'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, validators=[django.core.validators.MinValueValidator(1)])),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('likes_count', models.IntegerField(default=0)),
                ('associated_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.document')),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.profile')),
                ('replied_to_comment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='classbook_core.comment')),
            ],
        ),
        migrations.AddField(
            model_name='academicdegree',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.institution'),
        ),
    ]
