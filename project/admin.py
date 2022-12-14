from django.contrib import admin

from .models import Project, TypeUserStory, UserStory, TypeUserStoryStatus

admin.site.register(Project)
admin.site.register(TypeUserStoryStatus)
admin.site.register(TypeUserStory)
admin.site.register(UserStory)
