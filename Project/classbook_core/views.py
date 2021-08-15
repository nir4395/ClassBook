from sys import exc_info
from django.contrib.auth.forms import AuthenticationForm
from django.db.models.expressions import Exists
from django.http.request import split_domain_port
from django.shortcuts import render, redirect
from classbook_core.forms import SignUpForm, SignInForm
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http.response import FileResponse, JsonResponse, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from classbook_core.models import Course, Document, Institution, Profile, Comment
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.files.storage import FileSystemStorage, default_storage
from json import loads, dumps
from django.conf import settings

import os
from pathlib import Path
# from django.contrib.auth.decorators import login_required // Leon: we should use this decorator in the future.

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("sign_in") # TODO: change the redirect to the profile page / homepage

        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.error(request, error_string)

    form = SignUpForm
    return render(request=request, template_name="users/sign_up.html", context={"sign_up_form": form})


def sign_in(request):
    sign_in_successful = False

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(form)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                sign_in_successful = True
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('index')

        if not sign_in_successful:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.error(request, error_string)
            return redirect('sign_in')

    form = SignInForm()
    return render(request=request, template_name='users/sign_in.html', context={'sign_in_form': form})


# Construct the directory path in which the document-related file will be saved
def construct_file_save_directory(document):

    project_root_dir = settings.STORAGE_DIR
    directory_save_path = os.path.join(project_root_dir, 'courses', str(document.course.id))

    return directory_save_path

# Construct the full file path to retrieve document-related file from
def construct_file_path(document):

    project_root_dir = settings.STORAGE_DIR
    file_name_with_extension = '{0}.{1}'.format(document.name, document.doc_type) # Files are saved as 'name.doc_type'

    file_path = os.path.join(project_root_dir, 'courses', str(document.course.id), file_name_with_extension)

    return file_path

#
def find_available_file_name(original_uploaded_file_name, related_course):

    all_document_names_in_course = Document.objects.filter(course=related_course).values_list('name', flat=True)
    new_name = original_uploaded_file_name
    index = 1

    for record in all_document_names_in_course:
        print(record)

    while new_name in all_document_names_in_course:
        new_name = original_uploaded_file_name + ' ({0})'.format(index)
        index += 1

    return new_name


@require_http_methods(["GET"])
def course_docs(request, course_id, doc_category):
    try:

        # Get course from db by supplied course_id
        cur_course = Course.objects.get(pk=course_id)

        # Retrieve all course related documents
        course_documents = Document.objects.filter(course=cur_course, category=doc_category).values()

        # Convert ValuesQuerySet to list
        # Note that ValuesQuerySet has distinct elements while list does not
        course_documents_as_list = list(course_documents)
        
        print(course_documents_as_list)

        return JsonResponse({
            'id': course_id,
            'course_name': cur_course.name,
            'year_code': cur_course.year_code,
            'student count': cur_course.student_count,
            'documents' : course_documents_as_list
        })

    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')


# Returns categories of documents available for course
@require_http_methods(["GET"])
def course_categories(request, course_id):

    try:
        # Get course from db by supplied course_id
        cur_course = Course.objects.get(pk=course_id)

        # Retrieve all course related documents
        course_documents = Document.objects.filter(course=cur_course).values_list('category', flat=True)
        
        # Convert ValuesQuerySet to list
        # Note that ValuesQuerySet has distinct elements while list does not
        course_documents_as_list = list(course_documents)
        
        return JsonResponse({
            'categories' : course_documents_as_list
        })

    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')



@require_http_methods(["GET"])
def courses_by_year(request, ins_id, year_code_param):
    try:

        # Get course from db by supplied course_id
        courses_by_year = Course.objects.filter(pk = ins_id, year_code=year_code_param).values('name', 'id')
        courses_as_list = list(courses_by_year)
        print(courses_as_list)

        return JsonResponse({
            'courses_by_year': courses_as_list
        })
        
    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')


@require_http_methods(["GET"])
def document_by_id(request, doc_id):
    try:

        # Retrieve doc and update view count
        document = Document.objects.get(pk=doc_id)

        file_path = construct_file_path(document)
        file = open(file_path, 'rb')

        document.view_count += 1
        document.save()
        return FileResponse(file)

    # TODO - add exception for file opening failure
    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')

    except OSError:
        return HttpResponse('File error, either file is not found or directory is invalid.')

@require_http_methods(["POST"])
@csrf_exempt # Remove decorator after testing
def rate_document(request):

    try:

        # Retrieve doc and try to update rating
        # user_id = 1
        user_id = request.user.id

        data_as_dictionary = loads(request.body)
        document_id = data_as_dictionary['document_id']
        user_rating = data_as_dictionary['user_rating']

        current_document = Document.objects.get(pk=document_id)
        document_ratings = current_document.student_rated.all()
        user_profile = Profile.objects.get(pk=user_id)

        # Check if user already rated this document
        if not(document_ratings.filter(user_id=user_profile.user_id).exists()):
            print('Rating does not exist yet')

            # Calculate weighted mean and update document rating
            rating_count = document_ratings.filter(user_id=user_profile.user_id).count() + 1
            new_rating = (current_document.rating / rating_count) + (int(user_rating) / rating_count)
            current_document.rating = new_rating
            current_document.full_clean() # Verify data
            current_document.save() 

            # Mark that current user has rated the document
            current_document.student_rated.add(user_profile)
            
            return JsonResponse({
            'message' : 'Document rating accepted and updated successfully',
            'new rating' : new_rating
        })
        
        else:
            return HttpResponse("Rating for document by this user already exists.")
            
            
    except ValidationError:
        return HttpResponse('Rating is invalid or DB record is missing.')

    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')

def all_institutions(request):
    
    institutions = Institution.objects.all().values('id', 'name')
    institutions_as_list = list(institutions)

    return JsonResponse({
            'institutions': institutions_as_list
        })

@require_http_methods(["POST"])
@csrf_exempt # Remove decorator after testing
def upload_file(request):

    try:
        user_id = request.user.id

        # Retrieve JSON and uploaded file from request
        uploaded_file = request.FILES['file']
        json_accessory_data = request.POST

        # Get related course record from DB
        related_course_id = json_accessory_data['course_id']
        related_course = Course.objects.get(pk=related_course_id)
        related_user = Profile.objects.get(pk=user_id)

        # Construct file name format
        split_document_name_format = uploaded_file.name.rsplit('.', maxsplit=1)
        document_name = find_available_file_name(split_document_name_format[0], related_course)
        document_format = split_document_name_format[1]

        # Create new record for document in DB
        new_document = Document(name=document_name, course=related_course, author=related_user, doc_type=document_format, category='Exam')
        new_document.full_clean()
        new_document.save()

        file_save_directory = construct_file_save_directory(new_document)

        uploaded_file_name = '{0}.{1}'.format(new_document.name, new_document.doc_type)

        file_system = FileSystemStorage(file_save_directory)
        file_system.save(uploaded_file_name, uploaded_file)
        
        return HttpResponse('File uploaded successfully.')

    except ValidationError:
        print(exc_info())
        return HttpResponse('One of the document metadata parameters is invalid')

    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')


@require_http_methods(["POST"])
@csrf_exempt # Remove decorator after testing
def register_to_course(request):
    
    try:
        #user_id = 2
        user_id = request.user.id
        response = HttpResponse()

        data_as_dictionary = loads(request.body)
        course_id = data_as_dictionary['course_id']

        current_course = Course.objects.get(pk=course_id)
        current_profile = Profile.objects.get(pk=user_id)
        students_registered_in_course = current_course.student_enrolled.all()

        if not(students_registered_in_course.filter(pk=user_id).exists()):

            print('User is not yet registered to this course.')
            current_course.student_enrolled.add(current_profile)
            current_course.student_count += 1 # Increase student count
            current_course.save() # Update course DB record

            response = HttpResponse("User successfully registered to the course.")

        else:
            response = HttpResponse("User already registered to this course.")

        return response
            
    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')    


@require_http_methods(["POST"])
@csrf_exempt # Remove decorator after testing
def deregister_from_course(request):

    try:
        #user_id = 2
        user_id = request.user.id
        response = HttpResponse()

        data_as_dictionary = loads(request.body)
        course_id = data_as_dictionary['course_id']

        current_course = Course.objects.get(pk=course_id)
        current_profile = Profile.objects.get(pk=user_id)
        students_registered_in_course = current_course.student_enrolled.all()

        for record in students_registered_in_course:
            print(record)

        if students_registered_in_course.filter(pk=user_id).exists():

            print('User has registered to this course.')
            current_course.student_enrolled.remove(current_profile)
            current_course.student_count -= 1 # Decrease student count
            current_course.save() # Update course DB record

            response = HttpResponse("User successfully unregistered from the course .")

        else:
            response = HttpResponse("User isn't registered to this course and can't be unregistered from it.")

        return response
            
    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')   

@require_http_methods(["GET"])
@csrf_exempt # Remove decorator after testing
def courses_user_registered(request):

    try:
        #user_id = 2
        user_id = request.user.id

        current_profile = Profile.objects.get(pk=user_id)
        courses = Course.objects.filter(student_enrolled=current_profile).values('id', 'name', 'year_code', 'student_count', 'degree', 'date_updated')

        for record in courses:
            print(record)

        # Convert ValuesQuerySet to list of dictionaries
        # Note that ValuesQuerySet has distinct elements while list does not
        profile_courses_as_list = list(courses)

        return JsonResponse({
            'registered_courses: ': profile_courses_as_list,
        })
            
    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')   

    except ValidationError:
        return HttpResponse("Error when trying to validate new DB record.")


@require_http_methods(["POST"])
@csrf_exempt # Remove decorator after testing
def post_comment(request, doc_id):

    # get the comment information from this dictionary
    data_from_client_as_dictionary = loads(request.body) 
    comment_author = request.user.profile
    comment_content = data_from_client_as_dictionary['comment_content']

    # make sure the given document exists in the DB
    try:
        comment_associated_document = Document.objects.get(pk=doc_id)
    except:
        return HttpResponse("Error - document does not exist.Comment was not saved in the DB")

    # check if this comment is a reply to another comment
    replied_to_comment_id = data_from_client_as_dictionary['replied_to_comment_id']
    try:
        replied_to_comment = Comment.objects.get(pk=replied_to_comment_id)
    except Comment.DoesNotExist:
        replied_to_comment = None

    # save comment in the DB
    Comment(associated_document = comment_associated_document,
            author = comment_author,
            content = comment_content,
            replied_to_comment = replied_to_comment,
        ).save()

    if (replied_to_comment):
        return HttpResponse("Comment successfully saved in the DB (as a reply to another comment)")
    else:
        return HttpResponse("Comment successfully saved in the DB (not a reply)")



@require_http_methods(["GET"])
@csrf_exempt # Remove decorator after testing
def get_all_document_comments(request, doc_id):

    try:
        document = Document.objects.get(pk=doc_id)
    except Document.DoesNotExist:
        return JsonResponse('Document.DoesNotExist') # TODO: check if this is the correct way to return a django exception in Json format

    # TODO: check that the format of the json comments works as needed with the frontend
    return JsonResponse({
            'all_comments': str(document.get_all_comments_as_list())
        })
