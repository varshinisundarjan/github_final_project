```python
from django.urls import path
from . import views

app_name = "onlinecourse"

urlpatterns = [
    # URL for submitting the exam
    path('submit/<int:course_id>/', views.submit, name='submit'),

    # URL for showing exam results
    path(
        'course/<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='show_exam_result'
    ),
]
```
