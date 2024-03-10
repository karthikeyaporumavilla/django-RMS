# views.py
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import facultyRegister, Register, StudentRegister


def Homepage(request):
    return render(request, "Homepage.html")


def checkregistration(request):
    if request.method == "POST":
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirmPassword"]
        phoneNumber = request.POST["phoneNumber"]
        email = request.POST["email"]
        departmentId = request.POST["departmentId"]
        departmentName = request.POST["departmentName"]

        if password == confirmPassword:
            if Register.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect('signup')  # Replace 'signup' with the actual URL name for your signup page
            elif Register.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect('signup')  # Replace 'signup' with the actual URL name for your signup page
            else:
                user = Register.objects.create(firstName=firstName, lastName=lastName, username=username,
                                               password=password, phoneNumber=phoneNumber, email=email,
                                               departmentId=departmentId,
                                               departmentName=departmentName)
                user.save()
                messages.success(request, "User created successfully.")
                return render(request, "login.html")
        else:
            messages.error(request, "Password is not matching.")
            return redirect('signup')  # Replace 'signup' with the actual URL name for your signup page


def checkadminlogin(request):
    if request.method == "POST":
        user = request.POST["uname"]
        pas = request.POST["pwd"]

        if Register.objects.filter(username=user, password=pas).exists():
            messages.success(request, "This is admin TTM page.")
            return render(request, "adminhome.html")
        else:
            messages.error(request, "Your credentials are not correct.")
            return render(request, "loginfail.html")


def logout_view(request):
    logout(request)
    return redirect('Homepage')


def facultyRegistration(request):
    if request.method == "POST":
        firstName1 = request.POST["fname"]
        lastName1 = request.POST["lname"]
        username1 = request.POST["uname"]
        password1 = request.POST["pword"]
        confirmPassword1 = request.POST["cpassword"]
        phoneNumber1 = request.POST["pnumber"]
        email1 = request.POST["kmail"]
        departmentId1 = request.POST["did"]
        departmentName1 = request.POST["dname"]

        if password1 == confirmPassword1:
            if facultyRegister.objects.filter(uname=username1).exists():
                messages.error(request, "Username already exists.")
                return redirect('facultyRegistration')  # Replace 'signup' with the actual URL name for your signup page
            elif facultyRegister.objects.filter(kmail=email1).exists():
                messages.error(request, "Email already exists.")
                return redirect('facultyRegistration')  # Replace 'signup' with the actual URL name for your signup page
            else:
                user = facultyRegister.objects.create(fname=firstName1, lname=lastName1, uname=username1,
                                                      pword=password1, pnumber=phoneNumber1, kmail=email1,
                                                      did=departmentId1,
                                                      dname=departmentName1)
                user.save()
                messages.success(request, "User created successfully.")
                return render(request, "viewfaculty.html")
        else:
            messages.error(request, "Password is not matching.")
            return redirect('facultyRegistration')  # Replace 'signup' with the actual URL name for your signup page


def checkfacultylogin(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["pword"]

        # Check if the faculty user exists in the facultyRegister table
        if facultyRegister.objects.filter(uname=username, pword=password).exists():
            # If the user exists, you can add additional checks if needed

            # For simplicity, assuming login is successful, you can redirect to a faculty home page
            messages.success(request, "Login successful.")
            return render(request, "facultyhomepage.html")
        else:
            messages.error(request, "Invalid credentials.")
            return render(request, "loginfail.html")

    # return render(request, "facultylogin.html")


def viewfaculty(request):
    data = facultyRegister.objects.all()  # gets all the rows in the table
    return render(request, "viewfaculty.html", {"facultydata": data})


def update_faculty(request):
    if request.method == "POST":
        faculty_id = request.POST.get("faculty_id")
        faculty_instance = facultyRegister.objects.get(id=faculty_id)

        # Add your logic for updating faculty details here
        # You can render a separate update faculty form or perform the update directly

    return redirect('viewfaculty')  # Redirect to the faculty view after updating


def delete_faculty(request):
    if request.method == "POST":
        faculty_id = request.POST.get("faculty_id")
        faculty_instance = facultyRegister.objects.get(id=faculty_id)

        # Add your logic for deleting faculty here
        faculty_instance.delete()

    return redirect('viewfaculty')  # Redirect to the faculty view after deleting


def studentRegistration(request):
    if request.method == "POST":
        firstName1 = request.POST["first"]
        lastName1 = request.POST["last"]
        username1 = request.POST["user"]
        password1 = request.POST["p1"]
        confirmPassword1 = request.POST["cp1"]
        phoneNumber1 = request.POST["phone"]
        email1 = request.POST["mail"]
        departmentId1 = request.POST["Id"]
        departmentName1 = request.POST["department"]

        if password1 == confirmPassword1:
            if StudentRegister.objects.filter(username=username1).exists():
                messages.error(request, "Username already exists.")
                return redirect('studentRegistration')
            elif StudentRegister.objects.filter(email=email1).exists():
                messages.error(request, "Email already exists.")
                return redirect('studentRegistration')
            else:
                user = StudentRegister.objects.create(
                    first_name=firstName1,
                    last_name=lastName1,
                    username=username1,
                    password=password1,
                    phone_number=phoneNumber1,
                    email=email1,
                    department_id=departmentId1,
                    department_name=departmentName1
                )
                user.save()
                messages.success(request, "User created successfully.")
                return render(request, "viewstudent.html")
        else:
            messages.error(request, "Password is not matching.")
            return redirect('studentRegistration')


def viewstudent(request):
    data1 = StudentRegister.objects.all()  # gets all the rows in the table
    return render(request, "viewstudent.html", {"studentdata": data1})


def checkstudentlogin(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")

        # Check if the student user exists in the StudentRegister table
        if StudentRegister.objects.filter(username=username, password=password).exists():

            messages.success(request, "Login successful.")
            return render(request, "studenthomepage.html")

        else:
            messages.error(request, "Invalid credentials.")

    return render(request, "studentlogin.html")


def delete_student(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        student_instance = StudentRegister.objects.get(id=student_id)

        # Add your logic for deleting faculty here
        student_instance.delete()

    return redirect('viewstudent')




def faculty_home(request):
    total_students = StudentRegister.objects.count()
    students = StudentRegister.objects.all()  # Assuming StudentRegister is your model
    return render(request, 'facultyhomepage.html', {'students': students, 'total_students': total_students})


from django.shortcuts import render, redirect
from .models import Course


def course(request):
    if request.method == 'POST':
        course_code = request.POST.get('course_code')
        course_name = request.POST.get('course_name')
        department = request.POST.get('department')
        academic_year = request.POST.get('academic_year')

        Course.objects.create(
            course_code=course_code,
            course_name=course_name,
            department=department,
            academic_year=academic_year
        )
        return redirect('course')

    return render(request, 'course.html')


def view_courses(request):
    courses = Course.objects.all()
    return render(request, 'viewcourse.html', {'courses': courses})


from .models import ExamResult, Course, ExamType


def post_marks(request):
    if request.method == 'POST':
        id_value = request.POST.get('id')
        branch = request.POST.get('branch')
        course_code = request.POST.get('course')
        exam_type_name = request.POST.get('examType')  # Fetch exam type name from the form

        # Get or create ExamType instance based on the provided name
        exam_type, _ = ExamType.objects.get_or_create(name=exam_type_name)

        max_marks = request.POST.get('maxMarks')
        marks_obtained = request.POST.get('marksObtained')
        remarks = request.POST.get('remarks')

        # Get the Course instance based on the provided course code
        selected_course = Course.objects.get(course_code=course_code)

        # Create and save ExamResult instance
        ExamResult.objects.create(
            id=id_value,
            branch=branch,
            course=selected_course,
            exam_type=exam_type,
            max_marks=max_marks,
            marks_obtained=marks_obtained,
            remarks=remarks,
        )

        return redirect('post_marks')  # Redirect to the same page after form submission

    courses = Course.objects.all()
    return render(request, 'postMarks.html', {'courses': courses})


def view_exam_results(request):
    # Fetch all exam results
    exam_results = ExamResult.objects.all()

    # Get the ID from the request's GET parameters
    search_id = request.GET.get('search_id')

    # Filter results based on the entered ID
    if search_id:
        try:
            search_id = int(search_id)
            exam_results = exam_results.filter(id=search_id)
        except ValueError:
            # Handle the case where an invalid ID is entered
            pass

    return render(request, 'exam_results1.html', {'exam_results': exam_results})


def admin_view_exam_results(request):
    # Fetch all exam results
    exam_results = ExamResult.objects.all()

    # Get the ID from the request's GET parameters
    search_id = request.GET.get('search_id')

    # Filter results based on the entered ID
    if search_id:
        try:
            search_id = int(search_id)
            exam_results = exam_results.filter(id=search_id)
        except ValueError:
            # Handle the case where an invalid ID is entered
            pass

    return render(request, 'admin_exam_results.html', {'exam_results': exam_results})
