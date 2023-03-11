from django.contrib import admin
from .models import CodeInkForm
from .models import Uuser
from .models import cours
from .models import Lesson
# Register your models here.
@admin.register(CodeInkForm)
class FormAdmin(admin.ModelAdmin):
    list_display =['id','nam','surnam','passwor']

@admin.register(Uuser)
class UserAdmin(admin.ModelAdmin):
    list_display =['id','nam','surnam','passwor']


@admin.register(cours)
class CoursAdmin(admin.ModelAdmin):
    list_display=['id','description','category','image']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display=['id','course','fichier','title','description']
