from django.contrib import admin
from .models import *


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'obj')


admin.site.register(Animals)
admin.site.register(Bookmark, BookmarkAdmin)
