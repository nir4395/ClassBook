from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict


class Institution(models.Model):
    name = models.CharField(max_length=300)
    student_count = models.IntegerField(validators=[MinValueValidator(0)])
    academic_email_suffix = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @staticmethod
    def get_academic_instituion_choices():
        return list(Institution.objects.all().values_list('id','name'))


class AcademicDegree(models.Model):
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
    name = models.CharField(max_length=300)
    doc_type = models.CharField(max_length=10) # pdf, jpg, txt, cpp, cs, etc
    author = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='%(class)s_authors')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.CharField(max_length=300) # Exam, Notes, Homework Solutions etc
    view_count = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0.0)
    student_rated = models.ManyToManyField('Profile', related_name='%(class)s_students_rated') # Table for keeping track of which students rated the course
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_all_comments_and_replies_by_date(self):
        all_document_comments_by_date = Comment.objects.filter(associated_document=self).order_by('publish_date')
        comments_to_return = list()

        for current_comment in all_document_comments_by_date:
            # find the first(by date) non reply comment and add it the list
            if current_comment.replied_to_comment:
                continue
            comments_to_return.append(current_comment)

            # add all the replies to the current comment (by date)
            current_comment_replies = Comment.objects.filter(replied_to_comment=current_comment).order_by('publish_date')
            for reply in current_comment_replies:
                comments_to_return.append(reply)
    
        # convert all comment objects in the list to dictionary type to make Json converstion easier later
        for i in range(len(comments_to_return)): 
            comments_to_return[i] = model_to_dict(comments_to_return[i])

            # change author to author_name instead of author_id in the dictionary
            current_comment = comments_to_return[i]
            author_id = current_comment['author']
            current_comment['author'] = str(Profile.objects.get(pk=author_id))
            comments_to_return[i] = current_comment
           
        return comments_to_return


    def save(self, *args, **kwargs):
        
        # Convert document type and document category to lowercase upon creation
        self.doc_type = self.doc_type.lower()
        self.category = self.category.lower()
        return super(Document, self).save(*args, **kwargs)

    

class Comment(models.Model):
    associated_document = models.ForeignKey(Document, on_delete=CASCADE)
    author = models.ForeignKey(Profile, on_delete=CASCADE)
    content = models.TextField(max_length=500, validators=[MinLengthValidator(1)])
    publish_date = models.DateField(auto_now_add=True)
    replied_to_comment = models.OneToOneField('Comment', default=None, blank=True, null=True, on_delete=CASCADE)
    likes_count = models.IntegerField(default = 0)
