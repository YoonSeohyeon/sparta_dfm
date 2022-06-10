from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

# Register your models here.
admin.site.unregister(Group)

class HobbyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(UserModel)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel, HobbyAdmin)