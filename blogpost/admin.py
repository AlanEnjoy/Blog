from django.contrib import admin
from blogpost.models import Blogpost
from .models import Category, Tag, Blogpost

class BlogpostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug':('title',)}


admin.site.register([Category,Tag,Blogpost])
# Register your models here.
