from django.db import models


# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30, blank=False)
    lastName = models.CharField(max_length=30, blank=False)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)
    phoneNumber = models.CharField(max_length=30, blank=False, unique=True)
    email = models.CharField(max_length=30, blank=False, unique=True)
    departmentId = models.CharField(max_length=30, blank=False, unique=True)
    departmentName = models.CharField(max_length=30, blank=False)

    class Meta:
        db_table = "register_table"


class facultyRegister(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30, blank=False)
    lname = models.CharField(max_length=30, blank=False)
    uname = models.CharField(max_length=30, blank=False, unique=True)
    kmail = models.CharField(max_length=30, blank=False, unique=True)
    did = models.CharField(max_length=30, blank=False)
    dname = models.CharField(max_length=30, blank=False)
    pword = models.CharField(max_length=12, blank=False)
    pnumber = models.CharField(max_length=30, blank=False, unique=True)

    class Meta:
        db_table = "facultyregister_table"


class StudentRegister(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    department_id = models.CharField(max_length=10)
    department_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "studentregister_table"


class Course(models.Model):
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=10)

    class Meta:
        db_table = 'course_table'


class Department(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.name


class ExamType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'exam_type'

    def __str__(self):
        return self.name


class ExamResult(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    branch = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    max_marks = models.IntegerField()
    marks_obtained = models.IntegerField()
    remarks = models.TextField()

    class Meta:
        db_table = 'exam_result'

    def __str__(self):
        return f'{self.id} - {self.course.name} - {self.exam_type.name}'
