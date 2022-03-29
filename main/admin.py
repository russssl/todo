from encodings import search_function
from django.contrib import admin

from main.models import  ToDoList

from django.contrib.auth.models import Group

# admin.site.site_header=""
# admin.site.site_title=""
# admin.site.index_title = ""

admin.site.unregister(Group)


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['name','task_body','author','date_created','completed']
    list_filter = ['completed','date_created']

    search_fields = ["name",]

    actions = ["complete", "decomplete"]
    list_per_page = 50

    def complete(self, request,queryset):
        queryset.update(completed=True)
    complete.short_description = "Set Completed"

    def decomplete(self, request,queryset):
        queryset.update(completed=False)
    decomplete.short_description = "Unset Completed"


admin.site.register(ToDoList,ToDoListAdmin)