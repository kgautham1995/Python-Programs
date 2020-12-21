from django.contrib import admin
from app23.models import HODModel,FacultyModel,StudentModel,ParentModel
from django.contrib.auth.models import User,Group

# admin.site.register(HODModel)
admin.site.register(FacultyModel)
admin.site.register(StudentModel)
admin.site.register(ParentModel)

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(HODModel)
class HODAdmin(admin.ModelAdmin):
    list_display = ['idno','name','department','contactno','email','username','salary']

