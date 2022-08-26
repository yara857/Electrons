from django.contrib import admin
from .models import profile ,schedule ,Final , assignment 
from embed_video.admin import AdminVideoMixin
from .models import Uploads
# Register your models here.
admin.site.register(profile)
admin.site.register(schedule)
admin.site.register(Final)
admin.site.register(assignment)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Uploads, MyModelAdmin)