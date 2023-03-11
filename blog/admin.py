from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Contact


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    list_display = [
        "title",
        "date_created",
        "date_updated"
    ]
# admin.site.register(Model, Class)
admin.site.register(Post, PostAdmin) # Register Model
admin.site.register(Contact)
