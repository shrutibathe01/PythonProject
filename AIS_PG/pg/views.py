from django.shortcuts import HttpResponse, render ,redirect
import mariadb
from django.contrib import messages


Fname=''
Lname=''
Email=''
Password=''
First_Name=''
Last_Name=''
Email=''


name=''
contact_email=''
message=''

Full_Name=''
Pg_Name=''
Pg_Address=''
Pg_PhoneNo=''
EmailId=''
Password=''
Rent1=''
Rent2=''
Rent3=''
No_Members=''
Rent_Members=''
Food=''
Wifi=''
Furniture=''
Laundary=''
Parking=''
Image=''
No_SharingRent=''
SharingRent_1=''
SharingRent_2=''
MoreRent=''
Info=''



def mainDesktop(request):
    global Fname,Lname,Email,Password,Pg_Address
    if request.method=="POST":
        m=mariadb.connect(host="localhost",user="root",passwd="" ,database="ais_db")
        cursor=m.cursor()
        #tenent login
        if request.POST.get("submit")=='Login':
            data=request.POST
            for key,value in data.items():
                if key=='email1':
                    Email=value
                if key=='pass1':
                    Password=value
                          
            query="select * from tenantsignup where EmailId='{}' and Password='{}'".format(Email,Password)  
            cursor.execute(query)
            t=tuple(cursor.fetchall())
            
            if t==():
                return render(request,'TenantSignup.html') 
            else:
                query2="select Pg_Name,Pg_Address,id from owner"
                cursor.execute(query2)
                result=tuple(cursor.fetchall())               
                            
                return render(request,'tenantDashboard.html',{'result':result}) 
         
         #pg owner login  
        if request.POST.get("owner")=='Login':
            data=request.POST
            for key,value in data.items():
                if key=='email2':
                    Email=value
                if key=='pass2':
                    Password=value
                          
            query="select * from owner where EmailId='{}' and Password='{}'".format(Email,Password)  
            cursor.execute(query)
            t=tuple(cursor.fetchall())
            key=t[0][21]
            
            if t==():
                return render(request,'TenantSignup.html') 
            else:                
                query2="select * from owner where id='{}'".format(key)
                cursor.execute(query2)
                result=tuple(cursor.fetchall())
                return render(request,'ownerDashboard.html',{'result':result})        
            
        if request.POST.get("submit")=='search' :
            #return HttpResponse("search")
            data=request.POST
            for key,value in data.items():
                if key=='Pg_Address':
                     Pg_Address=value  
                    
            query="select * from owner where owner.Pg_Address LIKE '%{}%'".format(Pg_Address) 
            cursor.execute(query)
            t=tuple(cursor.fetchall())
            return render(request,'SearchPg.html',{'t':t}) 
    return render(request,'MainDesktop.html')

def ForgotP(request):
    return render(request,'forgotP.html')

def aboutUs(request):
    return render(request,'aboutUs.html')

def faq(request):
    return render(request,'faq.html')

def contact(request):
    global name,contact_email,message
    if request.method=="POST":
        m=mariadb.connect(host="localhost",user="root",password="",database="ais_db")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                name=value
            if key=="contact_email":
                contact_email=value
            if key=="message":
                message=value
                
        c="insert into contact values('{}','{}','{}')".format(name,contact_email,message)
        cursor.execute(c)
        m.commit()
        messages.success(request, 'Contact request submitted successfully.')
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')

def TenantSignup(request):
    global First_Name,Last_Name,Email,Password
    if request.method=="POST":
        m=mariadb.connect(host="localhost",user="root",password="",database="ais_db")
        cursor=m.cursor()
        d=request.POST
        
        for key,value in d.items():
            if key=="First_Name":
                First_Name=value
            if key=="Last_Name":
                Last_Name=value
            if key=="Email":
                Email=value
            if key=="Password":
                Password=value
        #return HttpResponse("Signup")
        c="insert into tenantsignup(First_Name,Last_Name,EmailId,Password) values('%s','%s','%s','%s')"%(First_Name,Last_Name,Email,Password)
        cursor.execute(c)
        m.commit()
        return render(request,'MainDesktop.html')
    return render(request,'TenantSignup.html')

def tenantDashboard(request):
    return render(request,'tenantDashboard.html')

def pgDetails(request,key):
    m=mariadb.connect(host="localhost",user="root",passwd="" ,database="ais_db")
    cursor=m.cursor()
    query="select * from owner where id='{}'".format(key)  
    cursor.execute(query)
    details=tuple(cursor.fetchall()) 
    return render(request,'PGDetails.html',{'details':details})

def Saved_Pg(request):
    return render(request,'Saved_Pg.html')


def OwnerSignup(request):
    global Full_Name,Pg_Name,Pg_Address,Pg_PhoneNo,EmailId,Password,Rent1,Rent2,Rent3,No_Members,Rent_Members,Food,Wifi,Furniture,Laundary,Parking,No_SharingRent,SharingRent_1,SharingRent_2,MoreRent,Info
    if request.method=="POST":
        m=mariadb.connect(host="localhost",user="root",password="",database="ais_db")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Full_Name":
                Full_Name=value
            if key=="Pg_Name":
                Pg_Name=value
                #return HttpResponse(Pg_Name)
            if key=="Pg_Address":
                Pg_Address=value
            if key=="Info":
                Info=value
               # return HttpResponse(Pg_Address)
            if key=="Pg_PhoneNo":
                Pg_PhoneNo=value
                #return HttpResponse(Pg_PhoneNo)
            if key=="EmailId":
                EmailId=value
               # return HttpResponse(EmailId)
            if key=="Password":
                Password=value
               # return HttpResponse(Password)
            if key=="Rent1":
                Rent1=value
            if key=="Rent2":
                Rent2=value
            if key=="Rent3":
                Rent3=value
            if key=="No_Members":
                No_Members=value
            if key=="Rent_Members":
                Rent_Members=value
            if key=="Food":
                Food=value
            if key=="Wifi":
                Wifi=value
            if key=="Furniture":
                Furniture=value
            if key=="Laundary":
                Laundary=value
            if key=="Parking":
                Parking=value 
            if key=="No_SharingRent":
                No_SharingRent=value
            if key=="SharingRent_1":
                SharingRent_1=value
            if key=="SharingRent_2":
                SharingRent_2=value
            if key=="MoreRent":
                MoreRent=value
            
                
        #return HttpResponse("data inserted successfully")       
        c="insert into owner(Full_Name,Pg_Name,Pg_Address,Info,Pg_PhoneNo,EmailId,Password,Rent1,Rent2,Rent3,No_Members,Rent_Members,Food,Wifi,Furniture,Laundary,Parking,No_SharingRent,SharingRent_1,SharingRent_2,MoreRent) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Full_Name,Pg_Name,Pg_Address,Info,Pg_PhoneNo,EmailId,Password,Rent1,Rent2,Rent3,No_Members,Rent_Members,Food,Wifi,Furniture,Laundary,Parking,No_SharingRent,SharingRent_1,SharingRent_2,MoreRent)
        cursor.execute(c)
        m.commit()
        #return HttpResponse("data inserted successfully")
        cursor.execute("select * from owner")
        result=tuple(cursor.fetchall())
        #return HttpResponse(result)
        #for x in result:
        #    print(x)
        return render(request,'OwnerDashboard.html')
    else:
        return render(request,'OwnerSignup.html')
    
def OwnerDashboard(request):
    return render(request,'OwnerDashboard.html')

Address=''
Profession=''
Gender=''

def RegisterTenant(request):
    global First_Name,Last_Name,EmailId,Address,Profession
    if request.method=="POST":
        m=mariadb.connect(host="localhost",user="root",password="",database="ais_db")
        cursor=m.cursor()
        d=request.POST
        
        for key,value in d.items():
            if key=="First_Name":
                First_Name=value
            if key=="Last_Name":
                Last_Name=value
            if key=="EmailId":
                EmailId=value
            if key=="Address":
                Address=value
            if key=="Profession":
                Profession=value
        #return HttpResponse("Signup")
        q="insert into TenantRegister(First_Name,Last_Name,EmailId,Address,Profession) values('%s','%s','%s','%s','%s')"%(First_Name,Last_Name,EmailId,Address,Profession)
        cursor.execute(q)
        m.commit()
       
    return render(request,'RegisterTenant.html')

def TenantInfo(request):
    m=mariadb.connect(host="localhost",user="root",passwd="" ,database="ais_db")
    cursor=m.cursor()
    query="select * from TenantRegister"
    cursor.execute(query)
    Info=tuple(cursor.fetchall()) 
    return render(request,'TenantInfo.html',{'Info':Info})

def DeleteTenant(request,key):
    #return HttpResponse(key)
    m=mariadb.connect(host="localhost",user="root",passwd="" ,database="ais_db")
    cursor=m.cursor()
    query="delete from TenantRegister where id='{}'".format(key)
    cursor.execute(query)
    m.commit()
    return redirect('TenantInfo')

"""def SearchPg(request,):
    m=mariadb.connect(host="localhost",user="root",passwd="" ,database="ais_db")
    cursor=m.cursor()
    query="select * from owner where owner.Pg_Address LIKE '%{}%'".format(Pg_Address)
    cursor.execute(query)
    t=tuple(cursor.fetchall())
    key=[0][21]
    if t==():
        return render(request,'MainDesktop.html') 
    else:
        query2="select Pg_Name,Pg_Address,id from owner where id='{}'".format(key)
        cursor.execute(query2)
        details=tuple(cursor.fetchall())               
        return render(request,'SearchPg.html',{'details':details}) 
    return render(request,'tenantDashboard.html',{'details'})"""
    
def SearchPg(request):
    return render(request,'SearchPg.html')

def OwnerInfo(request):
    m=mariadb.connect(host="localhost",user="root",passwd="" ,database="ais_db")
    cursor=m.cursor()
    query="select * from owner"
    cursor.execute(query)
    Info=tuple(cursor.fetchall()) 
    return render(request,'OwnerInfo.html',{'Info':Info})

def DeleteOwner(request,key):
    #return HttpResponse(key)
    m=mariadb.connect(host="localhost",user="root",passwd="" ,database="ais_db")
    cursor=m.cursor()
    query="delete from owner where id='{}'".format(key)
    cursor.execute(query)
    m.commit()
    return render(request,'MainDesktop.html')

def logout(request):
    return render(request,'MainDesktop.html')
    
def SearchPgDetails(request,key):
    m=mariadb.connect(host="localhost",user="root",passwd="" ,database="ais_db")
    cursor=m.cursor()
    query="select * from owner where id='{}'".format(key)  
    cursor.execute(query)
    details=tuple(cursor.fetchall()) 
    return render(request,'SearchPgDetails.html',{'details':details})

    
  
    