from django.urls import path
from . import views

urlpatterns = [
    path('', views.First_Page, name='First_Page'),
    path('MyHomePage.html', views.MyHomePage, name='MyHomePage'),
    path('AddNewStudent.html', views.AddNewStudent,name='AddNewStudent'),
    path('StudentSearch.html', views.StudentSearch, name='StudentSearch'),
    path('ViewAllStudents.html', views.ViewAllStudents, name='ViewAllStudents'),
    path('AddNewStudent/addX/', views.addX),
    path('getStudent/<int:sid>',views.getStudent),
    # path('StudentInfo.html/<int:sid>', views.getStudent), 
    
    path('ViewAllStudents.html/delete/<int:id>', views.delete,name='delete'),
    path('UpdateStudent.html/<int:id>',views.update,name='update'),
    path('UpdateStudent.html/updaterecord/<int:id>', views.updateRecord, name='updaterecord'),
    path('DepartmentAssignment.html/<int:id>',views.assign,name='assign'),
    path('DepartmentAssignment.html/assignRecord/<int:id>',views.assignRecord,name='assignrecord'),
]