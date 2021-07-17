from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Institution(models.Model):
    institution_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=300)
    student_count = models.IntegerField(validators=[MinValueValidator(0)])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.OneToOneField(Institution,null=True, on_delete=models.SET_NULL)
    birth_date = models.DateField(null=True, blank=True)

    # both methods will be triggered automatically after user.save is called
    # meaning - each time a user is created and saved - his profile object will also be created
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Year_Code(models.IntegerChoices):
    NONE = -2
    PRE = 0
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    OPTIONAL = 10

class Course(models.Model):
    course_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=300)
    student_count = student_count = models.IntegerField(validators=[MinValueValidator(0)])
    year_code = models.SmallIntegerField(Year_Code, default=Year_Code.NONE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

class Document(models.Model):
    doc_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=300)
    doc_type = models.CharField(max_length=10) # PDF, jpg, txt, cpp, c, etc
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    category = models.CharField(max_length=300) # Exam, Notes, Homework Solutions etc
    view_count = models.IntegerField(validators=[MinValueValidator(0)])
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    upload_date = models.DateField(auto_now_add=True)


