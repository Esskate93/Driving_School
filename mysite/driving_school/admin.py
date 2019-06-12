from django.contrib import admin

from .models import CustomUser
from .models import Planning
from .models import UserPlan

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Planning)
admin.site.register(UserPlan)
