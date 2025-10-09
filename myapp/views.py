from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
import random
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            msg = "User already exist"
            return render(request, 'signup.html', {'msg':msg})

        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mno = request.POST['mno'],
                    password = request.POST['password'],
                    profile = request.FILES['profile'],
                    usertype = request.POST['usertype']
                )
                msg = "Signup Succuessful"
                return render(request, 'signup.html', {'msg':msg})
            
            else:
                msg = "Password & confirm password doesn't match"
                return render(request, 'signup.html', {'msg':msg})
    else:
        return render(request, 'signup.html')
    

def login(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])

            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['profile']=user.profile.url

                if user.usertype=="pateint":
                    return redirect('index')
                
                else:
                    return redirect('dindex')
            
            else:
                msg = "Password does not match"
                return render(request, 'login.html', {'msg':msg})
        
        except:
            msg = "User doesn't exist, please signup"
            return render (request, 'login.html', {'msg':msg})
    else:
        return render(request, 'login.html')


def logout(request):
    del request.session['email']
    del request.session['profile']
    return redirect('index')            # we can also keep "login"

def fpass(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            otp = random.randint(1001,9999)

            subject = "OTP for Password Reset"
            message = f"""
                        Dear {user.name},

                        We received a request to reset your password. Please use the One-Time Password (OTP) below to proceed with resetting your account password:

                        Your OTP: {otp}

                        This OTP is valid for the next 10 minutes. Please do not share this code with anyone for security reasons. If you did not request a password reset, please ignore this email or contact our support team immediately.

                        Thank you,  
                        HealthCare Support Team
                        """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            
            send_mail(subject, message, email_from, recipient_list)

            request.session['email'] = user.email
            request.session['otp'] = otp
            return render(request, 'otp.html')
        
        except Exception as e:
            print("error",e)
            msg = "Email doesn't exist"
            return render (request, 'fpass.html', {'msg':msg})
    
    else:
        return render (request, 'fpass.html')


def otp(request):
    if request.method=="POST":
        try:
            otp = int(request.session['otp'])
            uotp = int(request.POST['uotp'])

            if otp==uotp:
                del request.session['otp']
                return render (request, 'newpass.html')
            else:
                msg = "Invalid OTP"
                return render (request, 'otp.html', {'msg':msg})
        
        except:
            pass
    
    else:
        return render (request, 'otp.html')
    

def newpass(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.session['email'])

            if request.POST['npassword']==request.POST['cnpassword']:
                user.password = request.POST['npassword']
                user.save()
                del request.session['email']
                return redirect('login')
            else:
                msg = "Passowr & confirm password does not match"
                return render (request, 'newpass.html', {'msg':msg})
        
        except:
            pass

    else:
        return render(request, 'newpass.html')
    

def changepass(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.session['email'])

            if user.password == request.POST['opassword']:
                if request.POST['npassword']==request.POST['cnpassword']:
                    user.password = request.POST['npassword']
                    user.save()
                    return redirect('logout')
                else:
                    msg = "New password & confirm new passowrd does not match"
                    return render(request, 'changepass.html', {'msg':msg})
            
            else:
                msg = "Your old password does not match"
                return render(request, 'changepass.html', {'msg':msg})
        
        except:
            pass
    
    else:
        return render(request, 'changepass.html')


def uprofile(request):
    user = User.objects.get(email=request.session['email'])

    if request.method=='POST':

        user.name = request.POST['name']
        user.mno = request.POST['mno']
        try:
            user.profile = request.FILES['profile']
            request.session['profile'] = user.profile.url   # session update, for profile image updatea
        except:
            pass
        user.save()

        if user.usertype=="pateint":
            return redirect('index')
        else:
            return redirect('dindex')
        
    else:
        if user.usertype=="pateint":
            return render(request, 'uprofile.html', {'user':user})

        else:
            return render(request, 'duprofile.html', {'user':user})


def dindex(request):
    try:
        pass
    except:
        pass
    return render(request, 'dindex.html')

def duprofile(request):
    try:
        pass
    except:
        pass
    return render(request, 'duprofile.html')

def add(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.session['email'])
            
            Doctor.objects.create(
                doctor = user,           # link this doctor to the logged-in user (from foreign key)
                cchoice = request.POST['cchoice'],
                dname = request.POST['dname'],
                demail = request.POST['demail'],
                qfc = request.POST['qfc'],
                charges = request.POST['charges'],
                address = request.POST['address'],
                start_time = request.POST['start_time'],
                end_time = request.POST['end_time'],
                exp = request.POST['exp'],
                dimage = request.FILES['dimage']
            )

            msg = "Doctor added successfully"
            return render(request, 'add.html', {'msg':msg})
        
        except Exception as e:
            print("******Error******", e)
            return redirect('dindex')
    
    else:
        return render(request, 'add.html')
    

def view(request):
    return render(request, 'view.html')