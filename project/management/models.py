from __future__ import unicode_literals
from django.db import models

from accounts.models import id_generator
from accounts.models import User
from extras import get_image_path

class StudentsManager(models.Manager):
    def create(self, f_name, l_name, dob=None):
        student = self.model(
            first_name=f_name,
            last_name=l_name,
            date_of_birth=dob,
        )

        student.save()
        return student

class Students(models.Model):
    student_id = models.CharField(max_length=6, null=True, blank=True, unique=True)
    portrait = models.ImageField(upload_to=get_image_path, default='/static/base/images/defaults/default-portrait.png')

    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    date_of_birth = models.DateField(blank=True, null=True)

    account = models.ForeignKey(User, blank=True, null=True)

    objects = StudentsManager()

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def add_account(self, account):
        if self.account is None:
            self.account = account
        self.save()

    def save(self):
        if not self.student_id:
            # Generate ID once, then check the db. If exists, keep trying.
            self.student_id = id_generator()
            while Students.objects.filter(student_id=self.student_id).exists():
                self.student_id = id_generator()
        super(Students, self).save()

# class TutorGroups(models.Model):
#     tutor_id = models.CharField(max_length=8)
#     description = models.TextField(max_length=255, null=True,
#                                   blank=False, default="No description given.")
#
# class Units(models.Model):
#     unit_code = models.CharField(max_length=35)
#     name = models.CharField(max_length=255)
#     description = models.TextField("Description", max_length=255, null=True,
#                                     blank=False, default="No description given.")
#
# # class Grades(models.Model):
# #     pass
#
# class Enrollment(models.Model):
#     student = models.ForeignKey(Students)
#     tutor = models.ForeignKey(TutorGroups)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False) #When object was created
#     updated_at = models.DateTimeField(auto_now=True) #When object was last updated
#     #grades = models.ForeignKey(Grades)
