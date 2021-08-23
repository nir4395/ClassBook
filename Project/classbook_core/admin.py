from classbook_core.models import Document, Profile, Course, Institution
from django.contrib import admin
from django.apps import apps


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return super(ListAdminMixin, self).get_readonly_fields(request, obj)

        # Filters results for institution admins (can only interact with records related to their own institution)
        elif request.user.groups.filter(name='Institution Admins').exists():

            current_user_institution = Profile.objects.get(user=request.user).institution

            # Courses query
            if isinstance(obj, Course):
                return ('institution', 'degree', 'student_count', 'date_created', 'date_updated')
            else:
                return super(ListAdminMixin, self).get_readonly_fields(request, obj)

        else:
            return None

    def get_queryset(self, request):
        qs = super(ListAdminMixin, self).get_queryset(request)

        # Returns full result for super admin
        if request.user.is_superuser:
            return qs

        # Filters results for institution admins (can only interact with records related to their own institution)
        elif request.user.groups.filter(name='Institution Admins').exists():

            current_user_institution = Profile.objects.get(user=request.user).institution

            # Courses query
            if qs.model is Document:
                return qs.filter(course__institution=current_user_institution)

            elif qs.model is Course:
                return qs.filter(institution=current_user_institution)
            else:
                return qs

        else:
            return None

    def delete_queryset(self, request, queryset):
        if queryset is Document:
            for record in queryset:
                record.delete()
        else:
            super(ListAdminMixin, self).delete_queryset(request, queryset)

# Data models that are designed to be managed by admins need to be registered here
# Currently registers all data models

models = apps.get_models()
for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
