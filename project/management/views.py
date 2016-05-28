from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from management.models import Students

@login_required
def home(request):
    student = get_object_or_404(Students, account=request.user)

    context = {
            'student': student,
    }
    return render(request, 'management/student_home.html', context)
