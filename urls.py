from django.urls import path
from . import views

urlpatterns=[
     path('',views.login, name='login'),
     path('course',views.course,name='course'),
     path('admin',views.admin,name='admin'),
     path('verify',views.verify,name='verify'),
     path('student',views.student,name='student'),
     path('register',views.register,name='register'),
     path('addsubject',views.addsubject,name='addsubject'),
     path('studentenroll',views.studentenroll,name='studentenroll'),
     path('viewsubject',views.viewsubject,name='viewsubject'),
     path('register1',views.register1,name='register1'),
     path('certificate',views.certificate,name='certificate'),
     path('genarate',views.genarate,name='genarate'),
     path('register2',views.register2,name='register2'),
]