```python
from django.contrib import admin
from .models import Course, Lesson, Instructor, Enrollment, Question, Choice, Submission

# Inline class to add choices within a question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Inline class to add questions within a lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


# Question admin configuration
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('content', 'grade')
    search_fields = ('content',)


# Lesson admin configuration
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'course')
    search_fields = ('title',)


# Register models in admin panel
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
```
