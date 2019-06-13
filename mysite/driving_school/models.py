from django.db import models
from django.db.models import Q
import django.contrib.admin


ROLE_CHOICE = (
    ("secretary", "secretary"),
    ("instructor", "instructor"),
    ("students", "students")
)

# Create your models here.

class User(models.Model):
    role = models.CharField(max_length=25, choices=ROLE_CHOICE)
    def __str__(self):
        return self.username

    @classmethod
    def _get_student(cls):
        return 1

class Planning(models.Model):
    date = models.DateTimeField('date')
    location = models.CharField(max_length=50)
    owner = models.ForeignKey(User,to_field='id', on_delete=models.CASCADE, related_name='owner', limit_choices_to=Q(role="secretary") | Q(role="instructor"))
    student = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name='user', limit_choices_to={"role": "students"})
    def __str__(self):
        return self.location

class UserPlan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    payed_hour = models.IntegerField(default=0)
    lessons = models.IntegerField(default=0)
    def __str__(self):
        return self.owner
