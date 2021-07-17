from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Institution(models.Model):
    institution_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=300)
    student_count = models.IntegerField(validators=[MinValueValidator(0)])

class AppUser(models.Model):
    # This field is the built-in django user model
    # We currently use the following attributes from the django user model: username, password, email, is_active
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=1)
    is_admin = models.BooleanField(default=False)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @staticmethod
    # Creates a new app_user (without superuser permissions) and saves it in the DB
    # The is_active attribute of AppUser.user is automatically set to 'True' when creating a new AppUser
    def create_app_user(username, email, password, admin_status):
        app_user = AppUser()
        user = User.objects.create_user(username, email, password)
        app_user.user = user
        app_user.is_admin = False
        app_user.institution_id = 1

        app_user.save()
        return app_user

    @staticmethod
    def get_all_app_users():
        return list(AppUser.objects.all())

    @staticmethod
    def get_app_user(username_to_find):
        try:
            user = User.objects.get(username=username_to_find)
            return AppUser.objects.get(user=user)

        except User.DoesNotExist:
            return None

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
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    category = models.CharField(max_length=300) # Exam, Notes, Homework Solutions etc
    view_count = models.IntegerField(validators=[MinValueValidator(0)])
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    upload_date = models.DateField(auto_now_add=True)


