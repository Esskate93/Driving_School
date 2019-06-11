from django.contrib import admin

from .models import User
from .models import Planning
from .models import UserPlan

# Register your models here.

admin.site.register(User)
admin.site.register(Planning)
admin.site.register(UserPlan)
