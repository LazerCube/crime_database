import django_tables2 as tables
from management.models import Students

from django_tables2.utils import A

class StudentsTable(tables.Table):
    student_id = tables.LinkColumn('management:student', args=[A('student_id')])
    first_name = tables.Column()
    last_name = tables.Column()
    date_of_birth = tables.DateColumn()
    account = tables.LinkColumn('accounts:student_account', args=[A('account.key')])

    class Meta:
        template = 'management/includes/table.html'
        attrs = {'class': 'table'}
