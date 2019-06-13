from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils import timezone


ROLE_CHOICE = (
    ("secretary", "secretary"),
    ("instructor", "instructor"),
    ("students", "students")
)

# Create your models here.

class CustomUser(AbstractUser):
    # username = models.CharField(max_length=50, unique=True)
    # password = models.CharField(max_length=256)
    role = models.CharField(max_length=25, choices=ROLE_CHOICE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    PASSWORD_FIELD = 'password'

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Planning(models.Model):
    date = models.DateTimeField('date')
    location = models.CharField(max_length=50)
    owner = models.ForeignKey(CustomUser,to_field='id', on_delete=models.CASCADE, related_name='owner', limit_choices_to=Q(role="secretary") | Q(role="instructor"))
    student = models.ForeignKey(CustomUser, to_field='id', on_delete=models.CASCADE, related_name='user', limit_choices_to={"role": "students"})
    def __str__(self):
        return self.location

class UserPlan(models.Model):
    creator = models.ForeignKey(CustomUser,to_field='id', on_delete=models.CASCADE, related_name='secretary', limit_choices_to={'role': 'secretary'}, default=None)
    user = models.ForeignKey(CustomUser, to_field='id', on_delete=models.CASCADE, related_name='students', limit_choices_to={"role": "students"}, default=None)
    payed_hour = models.IntegerField(default=0)
    lessons = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username