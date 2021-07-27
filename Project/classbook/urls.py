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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('users/sign_up/', views.sign_up, name='sign_up'),
    path('users/sign_in/', views.sign_in, name='sign_in'),
    # path('users/sign_out/', views.sign_out, name='sign_out'), // TODO: leon add signout 
    path('course/get/ins=<ins_id>,year=<year_code_param>', views.courses_by_year),
    path('course/get/course_id=<course_id>/categories', views.course_categories),
    path('course/get/course_id=<course_id>/cat=<doc_category>', views.course_docs),
    path('course/get/doc_id=<doc_id>', views.document_by_id),
    path('course/rate/doc_id=<doc_id>,rating=<rating>', views.rate_by_doc_id),
    path('sign_up/all_ins', views.all_institutions), # Get all supported institutions for sign-up droplist
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)