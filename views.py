```python
from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson, Question, Choice, Submission

# Function to submit exam answers
def submit(request, course_id):

    course = get_object_or_404(Course, pk=course_id)
    questions = Question.objects.filter(lesson__course=course)

    if request.method == "POST":
        submission = Submission.objects.create()

        selected_choices = []
        for question in questions:
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = Choice.objects.get(id=int(choice_id))
                selected_choices.append(choice)

        submission.choices.set(selected_choices)
        submission.save()

        context = {
            "course": course,
            "submission": submission
        }

        return render(request, "exam_result.html", context)

    context = {
        "course": course,
        "questions": questions
    }

    return render(request, "exam.html", context)


# Function to show exam result
def show_exam_result(request, course_id, submission_id):

    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_choices = submission.choices.all()

    total_score = 0
    total_grade = 0

    questions = Question.objects.filter(lesson__course=course)

    for question in questions:
        total_grade += question.grade

        correct_choices = question.choice_set.filter(is_correct=True)
        selected = selected_choices.filter(question=question)

        if set(correct_choices) == set(selected):
            total_score += question.grade

    context = {
        "course": course,
        "submission": submission,
        "score": total_score,
        "total": total_grade
    }

    return render(request, "exam_result.html", context)
```
