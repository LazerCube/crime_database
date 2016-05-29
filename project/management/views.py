from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django_tables2 import RequestConfig

from management.models import Students
from management.tables import StudentsTable
from management.forms import AddStudentForm

@login_required
def home(request):
    student = get_object_or_404(Students, account=request.user)

    context = {
            'student': student,
    }
    return render(request, 'management/student_home.html', context)

@login_required
def admin(request):
    if request.user.is_admin:
        table = StudentsTable(Students.objects.all())
        RequestConfig(request, paginate={"per_page": 25}).configure(table)

        context = {
            'table': table,
        }

        return render(request, 'management/admin.html', context)
    else:
        raise PermissionDenied

@login_required
def student(request, student):
    if request.user.is_admin:
        student = get_object_or_404(Students, student_id=student)

        context = {
            'student': student,
        }

        return render(request, 'management/student_home.html', context)
    else:
        raise PermissionDenied

@login_required
def add(request):
    if request.user.is_admin:
        title = 'Add new student'
        form = AddStudentForm(request.POST or None)
        if request.POST and form.is_valid():
            student = form.save()
            form = AddStudentForm()
            form.is_valid = True

        context = {
                'form': form,
                'title':title,
        }

        return render(request, 'management/forms/add.html', context)
    else:
        raise PermissionDenied
