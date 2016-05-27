from __future__ import unicode_literals
from django.db import models

import string

# def pkgen():
#     from base64 import b32encode
#     from hashlib import sha1
#     from random import random
#     rude = ('lol',) #list of strings you don't want as PK
#     bad_pk = True
#     while bad_pk:
#         pk = b32encode(sha1(str(random())).digest()).lower()[:6]
#         bad_pk = False
#         for rw in rude:
#             if pk.find(rw) >= 0:
#                 bad_pk = True
#     return pk

class StudentsManager(models.Manager):
    def create(self, f_name, l_name, dob):
        student = self.model(first_name=f_name,
                            last_name=l_name,
                            date_of_birth=dob,
                            )
        student.save()
        return student

class Students(models.Model):
    #student_id = models.CharField(max_length=6, primary_key=True, default=pkgen)
    student_id = models.CharField(max_length=6, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    date_of_birth = models.DateField(blank=True, null=True)

    objects = StudentsManager()

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return (('%s | %s'), self.student_id, self.get_full_name())

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def save(self):
        if not self.student_id:
            # Generate ID once, then check the db. If exists, keep trying.
            self.student_id = id_generator()
            while MyModel.objects.filter(student_id=self.student_id).exists():
                self.student_id = id_generator()
        super(MyModel, self).save()

#class classGroup(models.Model):
