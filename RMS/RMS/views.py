from django.shortcuts import render


def Homepage(request):
    return render(request, "Homepage.html")


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def facultylogin(request):
    return render(request, 'facultylogin.html')


def studentlogin(request):
    return render(request, 'studentlogin.html')


def facultyRegistration1(request):
    return render(request, 'addfaculty.html')


def studentRegistration1(request):
    return render(request, 'addstudents.html')


def adminhome(request):
    return render(request, 'adminhome.html')


def studenthomepage(request):
    return render(request, 'studenthomepage.html')
