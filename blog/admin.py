from django.contrib import admin
from .models import Post, Review, Project

admin.site.register(Post)

#admin.site.register(Skill)
#admin.site.register(Education)
#admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Review)
#admin.site.register(Service)
