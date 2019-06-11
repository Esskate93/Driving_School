from django.db import models
ROLE_CHOICE = (
    ("secretary", "secretary"),
    ("instructor", "instructor"),
    ("students", "students")
)

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=25, choices=ROLE_CHOICE)
    def __str__(self):
        return self.username

class Planning(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=50)
    owner = models.ForeignKey(User,to_field='id', on_delete=models.CASCADE, related_name='owner')
    student = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name='user')
    def __str__(self):
        return self.date

class UserPlan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    payed_hour = models.IntegerField(default=0)
    lessons = models.IntegerField(default=0)
    def __str__(self):
        return self.owner
