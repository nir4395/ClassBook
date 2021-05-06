from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class AppUser(models.Model):
    # This field is the built-in django user model
    # We currently use the following attributes from the django user model: username, password, email, is_active
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

    @staticmethod
    # Creates a new app_user (without superuser permmisions) and saves it in the DB
    # The is_active attribute of AppUser.user is automaticly set to 'True' when creating a new AppUser
    def create_app_user(username, email, password):
        app_user = AppUser()
        user = User.objects.create_user(username, email, password)
        app_user.user = user

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
