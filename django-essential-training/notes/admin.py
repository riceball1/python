from django.contrib import admin

from . import models

# need to set this up to appear in the admin
# must be done manually because otherwise will not show up in admin page
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Notes, NotesAdmin)