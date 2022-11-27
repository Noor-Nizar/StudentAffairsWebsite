from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from .models import Student
from django.contrib.auth import authenticate, login
def First_Page(request):
  template = loader.get_template('First_Page.html')
  return HttpResponse(template.render())

def AddNewStudent(request):
    template = loader.get_template('AddNewStudent.html')
    return HttpResponse(template.render({}, request))

def UpdateStudent(request):
    template = loader.get_template('UpdateStudent.html')
    return HttpResponse(template.render())

def MyHomePage(request):
    template = loader.get_template('MyHomePage.html')
    return HttpResponse(template.render())

def StudentSearch(request):
    template = loader.get_template('StudentSearch.html')
    return HttpResponse(template.render())

def ViewAllStudents(request):
  mymembers = Student.objects.all().values()
  template = loader.get_template('ViewAllStudents.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def addX(request):
    #gets all input variables from the form in AddNewStudent.html
    
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    id = request.POST.get('ID')
    gender = request.POST.get('gender')
    date_of_birth = request.POST.get('date_of_birth')
    New_student_Level = request.POST.get('New_student_Level')
    GPA = request.POST.get('GPA')
    Status = request.POST.get('Status')
    # department = request.POST.get('New_Student_department')
    #create new student
    new_student = Student(first_name=first_name, last_name=last_name, mail=email, phone=phone, id=id, gender=gender, date_of_birth=date_of_birth, level=New_student_Level, gpa=GPA, status=Status)
    new_student.save()
    return HttpResponseRedirect(reverse('ViewAllStudents'))

def add(request):
  template = loader.get_template("add.html")
  return HttpResponse(template.render({}, request))


def delete(request,id):
  myStudent = Student.objects.get(id=id)
  myStudent.delete()
  return HttpResponseRedirect(reverse('ViewAllStudents'))

def update(request, id):
  mymember = Student.objects.get(id=id)
  template = loader.get_template('UpdateStudent.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updateRecord(request,id):
  
  
  first = request.POST.get('firstname')
  last = request.POST.get('lastname')
  mail = request.POST.get('email')
  ph = request.POST.get('phone')
  sid = request.POST.get('ID')
  gend= request.POST.get('gender')
  dob = request.POST.get('date_of_birth')
  lev =request.POST.get('New_student_Level')
  gpa = request.POST.get('GPA')
  stat = request.POST.get('Status')

  member = Student.objects.get(id=id)
  
  member.first_name= first 
  member.last_name= last 
  member.mail= mail 
  member.phone= ph 
  member.id = sid
  member.gender= gend
  member.date_of_birth=dob 
  member.level=lev 
  member.gpa=gpa 
  member.status=stat 

  member.save()
  return HttpResponseRedirect(reverse('ViewAllStudents'))

  

def assign(request,id):
    mymember = Student.objects.get(id=id)
    template = loader.get_template('DepartmentAssignment.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def assignRecord(request,id):
  myStudent = Student.objects.get(id=id)
  if myStudent.level >= 3 and myStudent.level <=4 :
    myStudent.department = request.POST.get('Department')
    myStudent.save()
  return HttpResponseRedirect(reverse('ViewAllStudents'))



def getStudent(request, sid):
  myStudent = Student.objects.get(id=sid)
  template = loader.get_template('StudentInfo.html')
  context = {
    'x': myStudent,
  }
  return HttpResponse(template.render(context, request))