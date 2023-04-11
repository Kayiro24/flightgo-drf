from django.contrib import admin

# Register your models here.
class CreationModificationBaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    ordering = ['-created']

    def  get_list_display(self, request):
        return list(self.list_display) + ["created", "modified"]