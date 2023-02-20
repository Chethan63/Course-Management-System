from django.shortcuts import render
import mysql.connector
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

mydb=mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="class",
charset="utf8"

)
mycur = mydb.cursor()
def login(request):
    return render(request,'login.html')
    
def course(request):
    return render(request,'course.html')
    
def admin(request):
    return render(request,'admin.html')

def verify(request):
    if request.method=="POST":
        Username = request.POST.get("username")
        Password = request.POST.get("password")
        if Username=="admin" and Password=="1234":
            return render(request,"admin.html")
        else:
            sql="select * from student where reg='"+Username+"' and contact='"+Password+"'"
            mycur.execute(sql);
            if len(mycur.fetchall())>0:
                return render(request,"course.html")
            else:
                return render(request,"login.html",{"status":"Invalid UserName Or Password"})
          
def student(request):
    return render(request,'student.html')
    
def register(request):
    if request.method=="POST":
        reg = request.POST.get("reg")
        name = request.POST.get("name")
        fathername = request.POST.get("fathername")
        contact = request.POST.get("contact")
        gender = request.POST.get("gender")
        address = request.POST.get("address")        
        sql= "insert into student(reg,name,fathername,contact,gender,address) values(%s,%s,%s,%s,%s,%s)"
        val=(reg,name,fathername,contact,gender,address)
        mycur.execute(sql,val)
        mydb.commit()
        return render(request,"login.html")
        
def addsubject(request):
    return render(request,'addsubject.html')
    
def studentenroll(request):
    sql="select * from student"
    mycur.execute(sql);
    result = mycur.fetchall()
    return render(request,'studentenroll.html',{"res":result})
    
    
def viewsubject(request):
    return render(request,'viewsubject.html')
    
    
def register1(request):
    if request.method=="POST":
        reg = request.POST.get("reg")
        name = request.POST.get("name")
        course = request.POST.get("course")
        duration = request.POST.get("duration")
        fee = request.POST.get("fee")
        time = request.POST.get("time")
        sql="insert into subject (reg,name,course,duration,fee,time) values(%s,%s,%s,%s,%s,%s)"
        val=(reg,name,course,duration,fee,time)
        mycur.execute(sql,val)
        mydb.commit()
        return render(request,"admin.html")
        
        
def genarate(request):
    return render(request,'genarate.html')
        
        
def certificate(request):
    return render(request,'certificate.html')        
        
        
def register2(request):
    if request.method=="POST":
        reg = request.POST.get("reg")
        name = request.POST.get("name")
        course = request.POST.get("course")
        date = request.POST.get("date")
        print(date,name,course)
        li=[reg,name,course,date];
        return render(request,'certificate.html',{"result":date,"name":name,"course":course})

   
   