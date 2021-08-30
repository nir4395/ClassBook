"""classbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from classbook_core import views
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from classbook_core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('',login_required(TemplateView.as_view(template_name='index.html')), name='index'),

    # Users URLs
    path('users/sign_up/', views.sign_up, name='sign_up'),
    path('users/sign_in/', views.sign_in, name='sign_in'),
    path('users/sign_out/', views.sign_out, name='sign_out'),
    path('users/user_profile/', views.user_profile, name='user_profile'),
    path('users/user_profile/change_profile_details', views.change_profile_details, name='change_profile_details'),
    path('users/user_profile/upload_profile_picture', views.upload_profile_picture, name='upload_profile_picture'),

    # Course data requests
    path('course/get/ins/<ins_id>,year/<year_code_param>', views.courses_by_year),
    path('course/get/course_id/<course_id>/categories', views.course_categories),
    path('course/get/course_id/<course_id>/cat/<doc_category>', views.course_docs),
    path('course/get/doc_id/<doc_id>', views.document_by_id),

    path('sign_up/all_ins', views.all_institutions), # Get all supported institutions for sign-up droplist
    
    # Course data updates
    path('course/rate/', views.rate_document), 
    path('course/upload_file/', views.upload_file),
    path('course/register/', views.register_to_course),
    path('course/deregister/', views.deregister_from_course),
    path('course/user_registered/', views.courses_user_registered),

    # Document URLs
    path('doc_id/<doc_id>/post_comment', views.post_comment),
    path('doc_id/<doc_id>/get_all_document_comments', views.get_all_document_comments),
    path('doc_id/<doc_id>/is_document_rated_by_user', views.is_document_rated_by_user),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)