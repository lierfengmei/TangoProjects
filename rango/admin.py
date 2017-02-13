from django.contrib import admin
from .models import Category,Page
#from admin import ModelAdmin

#admin.site.register(Category)
#admin.site.register(Page)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

#Update the registration to include the customised interface
admin.site.register(Category,CategoryAdmin)

admin.site.register(Page,PageAdmin)

