from django.contrib import admin
from .models import Skills,About,Project,Contact

# Register your models here.
admin.site.register(Skills)
admin.site.register(About)
#admin.site.register(Project)
admin.site.register(Contact)

@admin.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)