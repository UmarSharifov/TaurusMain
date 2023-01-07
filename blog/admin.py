from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def get_form(self, request, *args, **kwargs):
        form = super(PostAdmin, self).get_form(request, **kwargs)
        form.user = request.user
        return form



class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)