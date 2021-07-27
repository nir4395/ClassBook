from django.shortcuts import render, redirect
from classbook_core.forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import FileResponse, JsonResponse, HttpResponse
from django.shortcuts import render
from classbook_core.models import Course, Document, Institution, Profile
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponseRedirect

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
            messages.error(request, "Unsuccessful registration. Invalid information.")

    form = SignUpForm
    return render(request=request, template_name="users/sign_up.html", context={"sign_up_form": form})


def sign_in(request):
    sign_in_successful = False

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

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
            messages.error(request, 'Invalid username or password.')
            return redirect('sign_in')

    form = AuthenticationForm()
    return render(request=request, template_name='users/sign_in.html', context={'sign_in_form': form})


def construct_file_path(document):

    project_dir = Path(__file__).resolve().parent.parent

    file_name_with_extension = '{0}.{1}'.format(document.name, document.doc_type)
    print(file_name_with_extension)
    file_path = os.path.join(project_dir, 'static', 'courses', str(document.doc_id), file_name_with_extension)
    print(file_path)

    return file_path


def course_docs(request, course_id, doc_category):
    try:

        print(doc_category)
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
            'course name': cur_course.name,
            'year_code': cur_course.year_code,
            'student count': cur_course.student_count,
            'documents' : course_documents_as_list
        })

    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')


# Returns categories of documents available for course
def course_categories(request, course_id):

    if request.method == 'GET':

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

    else: # Invalid method for resource
        return HttpResponse(content='Invalid request for resources', status=405)



def courses_by_year(request, ins_id, year_code_param):
    try:

        # Get course from db by supplied course_id
        courses_by_year = Course.objects.filter(institution_id = ins_id, year_code=year_code_param).values('name', 'course_id')
        courses_as_list = list(courses_by_year)
        print(courses_as_list)

        return JsonResponse({
            'courses_by_year': courses_as_list
        })
        
    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')


def document_by_id(request, doc_id):
    try:

        # Retrieve doc and update view count
        document = Document.objects.get(pk=doc_id)

        file_path = construct_file_path(doc)
        file = open(file_path, 'rb')

        document.view_count += 1
        document.save()
        return FileResponse(file)

    # TODO - add exception for file opening failure
    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')

    except OSError:
        return HttpResponseRedirect('File error, either file is not found or directory is invalid.')

def rate_by_doc_id(request, doc_id, rating):

    try:
        
        # Retrieve doc and update view count
        current_document = Document.objects.get(pk=doc_id)
        document_ratings = current_document.student_rated.all()
        user_profile = Profile.objects.get(pk=request.user.id) 

        print('User id: ' + str(user_profile.user_id))
        if document_ratings.filter(user_id=user_profile.user_id).exists():
            
            # Calculate weighted mean and update document rating
            rating_count = document_ratings.filter(user_id=user_profile.user_id).count() + 1
            new_rating = (current_document.rating / rating_count) + (int(rating) / rating_count)
            current_document.rating = new_rating

            current_document.full_clean() # Verify data
            current_document.save()
            return HttpResponse("Rating for this user and document already exists.")

        else:
            print('Rating does not exist yet')
            current_document.student_rated.add(user_profile)
            
    except ValidationError:
        print('Rating is incorrect')
        return HttpResponseRedirect('courses')

    except ObjectDoesNotExist:
        return HttpResponseRedirect('courses')

def all_institutions(request):
    
    institutions = Institution.objects.all().values('institution_id', 'name')
    institutions_as_list = list(institutions)

    return JsonResponse({
            'institutions': institutions_as_list
        })
