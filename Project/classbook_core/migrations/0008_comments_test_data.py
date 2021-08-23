from django.db import migrations, transaction
from classbook_core.models import Comment, Document, Profile
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('classbook_core', '0007_document_test_data')
    ]

    def generate_comments_test_data(apps, schema_editor):

        # get users and documents from the DB to use when creating comment test data
        profile_example_1 = Profile.objects.get(user=User.objects.get(username='leon123'))
        profile_example_2 = Profile.objects.get(user=User.objects.get(username='boaz77'))
        profile_example_3 = Profile.objects.get(user=User.objects.get(username='el4hjsda'))
        document_example_1 = Document.objects.get(name='hw4q1')
        document_example_2 = Document.objects.get(name='hw4q2')
        document_example_3 = Document.objects.get(name='חדוא 1 - תרגיל 5')


        # >>>>>>>>>>>>>>>>>>>>>>>>> comments
        comment_test_data = [
            #associated_document      author                    content                  replied_to_comment
            (document_example_1, profile_example_1, 'Great solution, helpmed me alot !',     None),
            (document_example_2, profile_example_1, 'I think there is a bug in this code',   None),
            (document_example_3, profile_example_3, 'Thanks for the help, good solution',    None),
            (document_example_3, profile_example_2, 'Thanks',                                None),
        ]

        with transaction.atomic():
            for associated_document, author, content, replied_to_comment in comment_test_data:
                Comment(associated_document=associated_document, author=author, content=content, replied_to_comment=replied_to_comment).save()
        

         # >>>>>>>>>>>>>>>>>>>>>>>>> replies
        comment_1 = Comment.objects.get(pk=1)
        comment_2 = Comment.objects.get(pk=2)
        comment_3 = Comment.objects.get(pk=3)

        reply_comments_test_data = [
            (document_example_1, profile_example_2, 'I agree with this comment',        comment_1),
            (document_example_2, profile_example_3, 'I also think there is a bug !',    comment_2),
            (document_example_3, profile_example_1, 'Agreed',                           comment_3),
        ]

        with transaction.atomic():
            for associated_document, author, content, replied_to_comment in reply_comments_test_data:
                Comment(associated_document=associated_document, author=author, content=content, replied_to_comment=replied_to_comment).save()

    operations = [
        migrations.RunPython(generate_comments_test_data),
    ]
