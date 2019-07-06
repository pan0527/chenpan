from django.contrib import admin
from .models import Question,Choices
# Register your models here.
class ChoicesInline(admin.StackedInline):
    model = Choices
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # list_display = ("desc","desc_date")
    inlines = [ChoicesInline,]

# class ChoicesAdmin(admin.ModelAdmin):
    # list_display = ("desc","votes","question")

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choices)