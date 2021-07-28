from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

class Institution(models.Model):
    institution_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=300)
    student_count = models.IntegerField(validators=[MinValueValidator(0)])
    accademic_email_suffix = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @staticmethod
    def print_test():
        print(Institution.objects.all())
        print(Institution.objects.all().values('institution_id', 'name'))


class AcademicDegree(models.Model):
    degree_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.user.username

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
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    degree = models.ForeignKey(AcademicDegree, on_delete=CASCADE)
    year_code = models.SmallIntegerField(Year_Code, default=Year_Code.NONE)
    student_enrolled = models.ManyToManyField('Profile')
    student_count = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Document(models.Model):
    doc_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=300)
    doc_type = models.CharField(max_length=10) # pdf, jpg, txt, cpp, cs, etc
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.CharField(max_length=300) # Exam, Notes, Homework Solutions etc
    view_count = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0.0)
    student_rated = models.ManyToManyField('Profile') # Table for keeping track of which students rated the course
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        
        # Convert document type and document category to lowercase upon creation
        self.doc_type = self.doc_type.lower()
        self.category = self.category.lower()
        return super(Document, self).save(*args, **kwargs)

class Comment(models.Model):
    associated_document = models.ForeignKey(Document, on_delete=CASCADE)
    auther = models.ForeignKey(Profile, on_delete=CASCADE)
    content = models.TextField(max_length=500, validators=[MinValueValidator(1)])
    publish_date = models.DateField(auto_now_add=True)
    replied_to_comment = models.OneToOneField('Comment', on_delete=CASCADE)
    likes_count = models.IntegerField(default = 0)
