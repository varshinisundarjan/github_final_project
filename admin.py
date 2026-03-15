from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission, Enrollment, User

# Inline class for Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Inline class for Question
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


# Admin configuration for Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('content', 'grade')
    search_fields = ['content']


# Admin configuration for Lesson
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'course')
    search_fields = ['title']


# Registering models in admin panel
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
