from django.shortcuts import render, redirect
from . import models
# Create your views here.


def Homepage(request):
    return render(request, 'index.html')


def Student_login(req):
    if req.method == "POST":
        uname = req.POST['username']
        pwd = req.POST['password']
        data = models.StudentDetails.objects.filter(
            username=uname, password=pwd)
        id = data[0].id
        return redirect(f'dashboard/{id}')
    return render(req, f'Student_login.html')


def Student_registration(req):
    if req.method == "POST":
        uname = req.POST['username']
        fname = req.POST['firstname']
        lname = req.POST['lastname']
        email = req.POST['emailId']
        pwd = req.POST['password']
        models.StudentDetails(username=uname, firstname=fname,
                              lastname=lname, emailId=email, password=pwd).save()
        return redirect('/student')
    return render(req, 'student_registration.html')


def stu_dashboard(request, id):
    modeldata = models.StudentDetails.objects.filter(id=id).values()[0]
    print(modeldata)

    return render(request, 'stu-dashboard.html', context={'data': modeldata})


"""Teacher section starts"""

def teacher_login(req):
    if req.method == "POST":
        uname = req.POST['username']
        pwd = req.POST['password']
        data = models.TeacherDetails.objects.filter(
            username=uname, password=pwd)
        id = data[0].id
        return redirect(f'tdashboard/{id}')
    return render(req, f'teacher_login.html')



def teacher_registration(req):
    if req.method == "POST":
        uname = req.POST['username']
        fname = req.POST['firstname']
        lname = req.POST['lastname']
        email = req.POST['emailId']
        pwd = req.POST['password']
        models.TeacherDetails(username=uname, firstname=fname,
                              lastname=lname, emailId=email, password=pwd).save()
        return redirect('/teacher')
    return render(req, 'teacher_registration.html')



def teac_dashboard(request, id):
    modeldata = models.TeacherDetails.objects.filter(id=id).values()[0]
    print(modeldata)

    return render(request, 'teac-dashboard.html', context={'data': modeldata})

"""teacher section ends"""

"""Assignemt section starts"""
def teacher_assignemt(req):
    if req.method == "POST":
        print("ABC")
        assignname = req.POST['nameassignment']
        assigndetails = req.POST['detailsassignment']
        stddetails = req.POST['std']
        models.TeacherAssignment(assignmentname=assignname, assignmentdetails=assigndetails, classdetails=stddetails).save()
        # return redirect(req,'/tdashboard')
    return render(req, 'teacher_assignment.html')


""" T - Assignemt section ends"""
""" T - Assignemt section starts"""


""" T - Assignemt section ends"""

""" S - Assignemt section starts"""

def student_assignment(req):

    mydata = models.TeacherAssignment.objects.filter(classdetails="12").values()
   
    return render(req,'student_assignment.html',context={"data":mydata})

""" S - Assignemt section ends"""





