from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CustomUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, unique=True, null=True)
    password = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    date_join = models.DateTimeField(default=timezone.now, editable=False)
    pk = User.pk
    PASSWORD_FIELD = 'password2'
    set_password = "password2"
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.user} Profile'

