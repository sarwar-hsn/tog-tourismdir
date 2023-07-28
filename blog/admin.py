from django.contrib import admin
from .models import Author,Category,Tag,Post,PostImages,BanglaBlog,BanglaPostImages,CategoryBangla
from django import forms
from django.forms import CheckboxSelectMultiple



admin.site.register(Author)
admin.site.register(Category)
admin.site.register(CategoryBangla)
admin.site.register(Tag)

class PostImagesAdmin(admin.StackedInline):
    model = PostImages

class PostAdmin(admin.ModelAdmin):
    inlines =[PostImagesAdmin]
    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['tags'].widget = forms.CheckboxSelectMultiple()
        return form

admin.site.register(Post,PostAdmin)


class BanglaPostImagesAdmin(admin.StackedInline):
    model = BanglaPostImages
class BanglaBlogAdmin(admin.ModelAdmin):
    inlines =[BanglaPostImagesAdmin]

admin.site.register(BanglaBlog,BanglaBlogAdmin)



