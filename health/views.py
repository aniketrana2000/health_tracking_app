from pickle import FALSE
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.messages import constants as messages
from health.models import *
from random import randint
from itertools import combinations
from functools import reduce
from operator import add
from django.db.models import Sum
from datetime import datetime , date , timedelta
from django.utils import timezone
import random



def home(request):
    if "id" in request.session:
        user3=UserModel.objects.get(user_id=request.session["id"])

        if request.session["role"]=="As a User":
            if user3.expirydate:
              if user3.expirydate<=timezone.now():
                date=user3.expirydate
                date.delete()
                return render(request, "health/home.html",{"expirydate":user3.expirydate})
              return render(request, "health/home.html",{"expirydate":user3.expirydate})
            return render(request, "health/home.html",{"expirydate":user3.expirydate})
        if request.session["role"]=="As a Admin":
            print("#############eeeee#############")
            return render(request, "health/home2.html")
    return render(request, "health/home1.html")

   

def adminhome(request):
    return render(request, "health/adminhome.html")



def RegisterUser(request):
    if request.method=="POST":
        if request.POST['role']=="As a User":
            first_name= request.POST['first_name']
            last_name= request.POST['last_name']
            contact_no= request.POST['contact_no']
            email= request.POST['email']
            username=request.POST['username']
            password= request.POST['password']
            cpassword= request.POST['cpassword']
            role=request.POST['role']
            Gender=request.POST['gender']

            user = User.objects.filter(email=email)
            user9=User.objects.filter(username=username)
            user8=UserModel.objects.filter(contact_no=contact_no)
            if user:
                message="User Already Exists"
                return render(request, "health/signup.html", {"msg":message})
            elif user9:
                message="Username Already Exists"
                return render(request, "health/signup.html", {"msg":message})
            elif user8:
                message="Mobile Number Already Exists"
                return render(request, "health/signup.html", {"msg":message})
            else:
                if password == cpassword:
                    print(password,"#########################")
                    password=make_password(password)
                    user1=User.objects.create(password=password, email=email,first_name=first_name, last_name=last_name, username=username)
                    user2=UserMaster.objects.create(user_id=user1,role=role)
                    newuser=UserModel.objects.create(user_id=user2,contact_no=contact_no,Gender=Gender)
                    return redirect("login")
    
        if request.POST['role']=="As a Admin":
            first_name= request.POST['first_name']
            last_name= request.POST['last_name']
            contact_no= request.POST['contact_no']
            email= request.POST['email']
            username=request.POST['username']
            password= request.POST['password']
            cpassword= request.POST['cpassword']
            role=request.POST['role']
            Gender=request.POST['gender']

            user = User.objects.filter(email=email)

            if user:
                print("736373333333")
                message="User Already Exists"
                return render(request, "health/signup.html", {"msg":message})

            if request.POST["pas"]=="HMRITM@1234":
                if password == cpassword:
                    print(password,"#########################")
                    password=make_password(password)
                    user1=User.objects.create(password=password, email=email,first_name=first_name, last_name=last_name, username=username)
                    user1.is_staff=1
                    user1.is_superuser=1
                    user1.save()
                    user2=UserMaster.objects.create(user_id=user1,role=role)
                    user3= UserModel.objects.create(user_id=user2,contact_no=contact_no,Gender=Gender)
                    return redirect("login")
            else:
                    message="admin password is not correct please check"
                    return render(request, "health/signup.html", {"msg":message})
    return render(request, "health/signup.html")


def LoginUser(request):
    if request.method=="POST":
            email= request.POST['email']
            password= request.POST['password']
            print(password,"###################")
            user1= User.objects.filter(email=email)
            print(user1,"###########")
            if user1:
                user2= UserMaster.objects.get(user_id=user1[0].id)
                if check_password(password,user1[0].password):
                    print(user2.id,"zzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
                    user3= UserModel.objects.get(user_id=user2.id)
                    print(user1[0].id,"EEEEEEEEEEEEEEEEEEEE")
                    request.session["id"]=user1[0].id
                    request.session["role"]=user2.role
                    print(request.session["id"],"######################")
                    return redirect('home')
                elif check_password(password,user1[0].password) and user1[0].is_staff==1 and user1[0].is_superuser==1:
                    user2= UserMaster.objects.get(user_id=user1[0].id)
                    print(user2.role,"###########")
                    print(user1[0].id,"RRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                    request.session["id"]=user1[0].id
                    request.session["role"]=user2.role
                    print(request.session["id"],"######################")
                    print(request.session["role"],"######################")
                    return redirect('home')

                else:
                    message="Password doesnot match"
                    return render(request,"health/login.html", {'msg':message})
            else:
                message="User doesnot exist"
                return render(request,"health/login.html", {'msg':message})

    return render(request,"health/login.html")

def logout(request):
            print(request.session["id"],"##########hello#######")
            del request.session["id"]
            return redirect("login")

def ProfilePage(request, pk):
  if request.session["id"]:
    user1=User.objects.get(pk=pk)
    user2=UserMaster.objects.get(user_id=user1.id)
    user3=UserModel.objects.get(user_id=user2.id)
    return render(request, "health/profile.html", {"user1":user1 ,"user3":user3,"user2":user2})
  return(request,"health/login.html")

def UpdateProfile(request,pk):
    user1=User.objects.get(pk=pk)
    user2=UserMaster.objects.get(user_id=user1.id)
    user3=UserModel.objects.get(user_id=user2.id)
    if request.method == "POST":
        if user2.role=="As a User":
            user1.first_name=request.POST['first_name']
            user1.last_name=request.POST['last_name']
            user1.username=request.POST['username']
            user3.contact_no=request.POST['contact_no']
            user3.vegnonveg=request.POST['vegnonveg']
            user3.Age=request.POST['Age']
            user3.Height=request.POST['Height']
            user3.Weight=request.POST['Weight']
            user1.save()
            user3.save()
            return render(request, "health/profile.html", {"user1":user1 ,"user3":user3})
        if user2.role=="As a Admin":
            user1.first_name=request.POST['first_name']
            user1.last_name=request.POST['last_name']
            user1.username=request.POST['username']
            user3.contact_no=request.POST['contact_no']
            user1.save()
            user3.save()
            return render(request, "health/profile.html", {"user1":user1 ,"user3":user3})
    else:
        return render(request, "health/update.html", {"user1":user1 ,"user3":user3})



def bmi(request,pk):
    user1=User.objects.get(pk=pk)
    user2=UserMaster.objects.get(user_id=user1.id)
    user3=UserModel.objects.get(user_id=user2.id)

    if  user3.Height is None or user3.Weight is None:
        msg="Please first update your profile"
        return render(request,"health/calculatebmi.html", {"msg":msg})
    try:
        height=user3.Height
        weight=user3.Weight
        try:
           bmi=round(weight/((height/100)*(height/100)),2)
        except:
             msg="Please Correct Your Profile Details"
             return render(request,"health/profile.html",{"msg":msg})
        age=user3.Age
        try:
           if user3.Gender == "male":
              BMR=round(88.362+(13.397*weight)+(4.799*height)-(5.677*age),2)
           else:
              BMR=round(447.593+(9.247*weight)+(3.098*height)-(4.330*age),2)
        except:
              msg="Please enter valid Number"
              return render(request,"health/profile.html",{"msg":msg})
        return  render(request,"health/calculatebmi.html",{"bmi":bmi,"CURRENT_BMR":BMR})
    
    except:
          msg="Please enter valid Number"
          return render(request,"health/profile.html",{"msg":msg})

def goalbmi(request,pk):
    msg=""
    user1=User.objects.get(pk=pk)
    user2=UserMaster.objects.get(user_id=user1.id)
    user3=UserModel.objects.get(user_id=user2.id)
    if  user3.Height is None or user3.Weight is None:
        msg= msg="please first update your profile"
        return render(request,"health/bmigoal.html", {"msg":msg})

   
    elif request.POST.get("goalweight") is None:
        msg="Set Your Goal"
        return render(request,"health/bmigoal.html", {"msg":msg})
    try: 
        height=user3.Height
        weight1=int(request.POST["goalweight"])
        user3.goalweight=weight1
        user3.save()
        try:
            goalbmi=round(weight1/((height/100)*(height/100)),2)
        except:
                msg="Please enter valid Number or check your profile"
                return render(request,"health/bmigoal.html",{"msg":msg})
        age=user3.Age

        try:
            if user3.Gender == "male":
                ABMR=round(88.362+(13.397*weight1)+(4.799*height)-(5.677*age),2)
            else:
                ABMR=round(447.593+(9.247*weight1)+(3.098*height)-(4.330*age),2) 
        except:
                msg="Please enter valid number"
                print(ABMR,"___________________________")
                return render(request,"health/bmigoal.html",{"msg":msg})
        return  render(request,"health/bmigoal.html",{"goalbmi":goalbmi,"AIM_BMR":ABMR,"msg":msg})   # render_template("bmi.html")
    except:
          msg="Please enter valid number"
          print(ABMR,height,weight1,goalbmi,age,"@@@@@@@@@@@@@@@@@@@@@@@")
          return render(request,"health/bmigoal.html",{"msg":msg})
    

def diet(request,AIM_BMR,pk):
    AIM_BMR=float(AIM_BMR)
    user1=User.objects.get(pk=pk)
    user2=UserMaster.objects.get(user_id=user1.id)
    user3=UserModel.objects.get(user_id=user2.id)
    b_bmr=AIM_BMR/4
    l_bmr=AIM_BMR/2
    if AIM_BMR>2926.217:
        msg="please set goal less than 170 KG"
        return render(request,"health/bmigoal.html",{"msg":msg})
    if user3.vegnonveg is None:
         msg="Please first add your preference You are vegetarian or non vegetarian"
         return render(request,"health/profile.html",{"msg":msg})
    if user3.vegnonveg=="veg":
        x=Breakfast.objects.filter(Bvn="veg").all()
        p=[(e.id, e.Breakfastcalorie, e.Breakfastfood) for e in x]
        calories=[e[1] for e in p]
        match_sum = [] 
        print(p,"------------")
        for i in range(1,len(calories)): 
            x = list(combinations(calories, i)) 
            for matches in x: 
                tmp = reduce(add, matches) 
                if b_bmr<=tmp<=b_bmr+20: 
                    match_sum.append(matches) 
                    match_sum.sort()   
        bl=[]
        l=[]
        for e in match_sum[0]:
            b1=tmp = reduce(add, match_sum[0]) 
            for j in p:    
                if e==j[1] and j[0] not in l:
                    l.append(j[0])
                    bl.append(j[2])
                    break  
         
        
        y=Dinner.objects.filter(Dvn="veg").all()
        p=[(e.id, e.Dinnercalorie, e.Dinnerfood) for e in y]
        print(p,"###################")
        calories=[e[1] for e in p]
        match_sum = [] 
        for i in range(1,len(calories)): 
            x = list(combinations(calories, i)) 
            for matches in x: 
                tmp = reduce(add, matches) 
                if b_bmr<=tmp<=b_bmr+20: 
                    match_sum.append(matches)   
        print(match_sum,"#####################")
        dl=[]
        l=[]
        for e in match_sum[0]:
            d1= reduce(add, match_sum[0]) 
            for j in p:   
                if e==j[1] and j[0] not in l:
                    l.append(j[0]) 
                    dl.append(j[2])
                    break  

        z=Lunch.objects.filter(Lvn="veg").all()
        p=[(e.id, e.Lunchcalorie, e.Lunchfood) for e in z]
        print(p,"###################")
        calories=[e[1] for e in p]
        match_sum = [] 
        for i in range(1,len(calories)): 
            x = list(combinations(calories, i)) 
            for matches in x: 
                tmp = reduce(add, matches) 
                if l_bmr<=tmp<=l_bmr+20: 
                    match_sum.append(matches)   
        print(match_sum,"#####################")
        ll=[]
        l=[]
        for e in match_sum[0]:
            l1= reduce(add, match_sum[0]) 
            for j in p:   
                if e==j[1] and j[0] not in l:
                    l.append(j[0]) 
                    ll.append(j[2])
                    break  
    else:
        x=Breakfast.objects.filter().all()
        p=[(e.id, e.Breakfastcalorie, e.Breakfastfood) for e in x]
        calories=[e[1] for e in p]
        match_sum = [] 
        for i in range(1,len(calories)): 
            x = list(combinations(calories, i)) 
            for matches in x: 
                tmp = reduce(add, matches) 
                if b_bmr<=tmp<=b_bmr+20: 
                    match_sum.append(matches) 
        l=[]
        bl=[]
        for e in match_sum[0]:
            b1= reduce(add, match_sum[0]) 
            for j in p:    
                if e==j[1] and j[0] not in l:
                    l.append(j[0])
                    bl.append(j[2])
                    break  
        
        y=Dinner.objects.filter().all()
        p=[(e.id, e.Dinnercalorie, e.Dinnerfood) for e in y]
        calories=[e[1] for e in p]
        match_sum = [] 
        for i in range(1,len(calories)): 
            x = list(combinations(calories, i)) 
            for matches in x: 
                tmp = reduce(add, matches) 
                if b_bmr<=tmp<=b_bmr+20: 
                    match_sum.append(matches) 
        l=[]
        dl=[]
        for e in match_sum[0]:
            d1= reduce(add, match_sum[0]) 
            for j in p:    
                if e==j[1] and j[0] not in l:
                    l.append(j[0])
                    dl.append(j[2])
                    break 

        z=Lunch.objects.filter().all()
        p=[(e.id, e.Lunchcalorie, e.Lunchfood) for e in z]
        calories=[e[1] for e in p]
        match_sum = [] 
        for i in range(1,len(calories)): 
            x = list(combinations(calories, i)) 
            for matches in x: 
                tmp = reduce(add, matches) 
                if l_bmr<=tmp<=l_bmr+20: 
                    match_sum.append(matches) 
        l=[]
        ll=[]
        for e in match_sum[0]:
            l1= reduce(add, match_sum[0]) 
            for j in p:    
                if e==j[1] and j[0] not in l:
                    l.append(j[0])
                    ll.append(j[2])
                    break   
    print(bl,"#######")
    return render(request,"health/diet.html",{"l1":bl,"l3":ll,"l2":dl,"b":b1,"d":d1,"l":l1})


def foodlist(request,l1=None,s=None):
    user_id=UserMaster.objects.get(id=request.session["id"])
    user_intake=UserIntakeModel.objects.filter(user_id=request.session["id"]).all()
    x=intakediet.objects.all()
    foodlist=[e.intakefood for e in x]
    ufood=request.POST.get("food")
    print(ufood,"################")
    l1=l1
    print(l1,"kkkkkkkkk234kkkkkkkk")
    s=s
    print(s,"kkkkkkkkkkk234kkkkkk")
    if ufood is None and l1 and s:
            print("#######################np###")
            user_intake=UserIntakeModel.objects.filter(user_id=user_id).all()
            return render(request,"health/intakecalorie.html",{"food":foodlist, "data":user_intake,"l":l1,"s":s})
    if ufood is None and l1 is None and s is None:
            print("#######################np###")
            user_intake=UserIntakeModel.objects.filter(user_id=user_id).all()
            cal_list= [ cal.calorie for cal in user_intake]
            print(cal_list,"#####nitin###")
            total_cal=sum(cal_list)
            length=len(user_intake)
            print(user_intake,"##############")
            return render(request,"health/intakecalorie.html",{"food":foodlist, "data":user_intake,"l":length,"s":total_cal})
    if request.method=="POST":
        if ufood is None and l1 is None and s is None:
            print("#######################gt###")
            return render(request,"health/intakecalorie.html",{"food":foodlist})
        
        y=intakediet.objects.filter(intakefood=ufood).all()
        print(y,"!!!!!!!!!!!!!")
        l=[]
        for e in y:
            p=e.intakecalorie
            l.append(p)
        intake_food=ufood
        print(l,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        intake_calorie=l[-1]
        user_intake=UserIntakeModel.objects.create(food=intake_food, calorie=intake_calorie, user_id=user_id)
        
        user_intake=UserIntakeModel.objects.filter(user_id=user_id).all()
        cal_list= [ cal.calorie for cal in user_intake]
        print(cal_list,"#####nitin###")
        total_cal=sum(cal_list)
        length=len(user_intake)
        print(user_intake,"##############")
        return render(request,"health/intakecalorie.html", {"l":length, "data":user_intake,"food":foodlist,"s":total_cal})
    return render(request,"health/intakecalorie.html", {"food":foodlist,"data":user_intake})

def delete_diet(request):
    user_id=UserMaster.objects.get(id=request.session["id"])
    id=request.POST["cancel"]
    print(id,"&&&&&&&&&&&&&&&&&&*****")
    row=UserIntakeModel.objects.get(id=id)
    print(row,"#################")
    row.delete()
    user_intake=UserIntakeModel.objects.filter(user_id=user_id).all()
    cal_list= [ cal.calorie for cal in user_intake]
    print(cal_list,"#####nitin###")
    total_cal=sum(cal_list)
    l1=request.POST["length1"]
    print(l1,"$$$$$$$$$44444444444444444444444444444444")
    return redirect("foodlist", l1=l1, s=total_cal)



def water(request,pk):
    user1=User.objects.get(pk=pk)
    user2=UserMaster.objects.get(user_id=user1.id)
    user3=UserModel.objects.get(user_id=user2.id)
    return render(request,"health/water")


def about(request):
    return render(request, "health/about.html")

def contact(request):
    return render(request, "health/contact.html")

def Trainerlist(request):
    user1=TrainerModel.objects.all()
    return render(request, "health/Trainerlist.html",{"user1":user1})

def view_profile(request,id):
    user=TrainerModel.objects.filter(id=id)
    print(user,"***************************")
    return render(request, "health/Modal.html",{"user":user})

def Videos1(request):
  if request.session["id"] is not None:
    user1=UserModel.objects.get(id=request.session["id"])
    if user1.Weight is None or user1.Height is None or user1.Age is None:
        msg="First Update Your Profile"
        return render(request,"health/profile.html",{"msg":msg})
    elif user1.goalweight is None:
        msg="First Set Your Goal"
        return render(request,"health/bmigoal.html",{"msg":msg})
    else:
        if user1.Weight >user1.goalweight:
            videos1=Videos.objects.filter(field="Loss").all()
            videos=random.sample(list(videos1), 5)

            return render(request,"health/videos.html",{"videos":videos})
        if user1.Weight <user1.goalweight:
            videos1=Videos.objects.filter(field="Gain").all()
            videos=random.sample(list(videos1), 5)

            return render(request,"health/videos.html",{"videos":videos})
  else:
      return render(request,"health/login.html")

def savevideo(request,id):
    user1=User.objects.get(pk=request.session["id"])
    print(user1.id,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    user2=UserMaster.objects.get(user_id=user1.id)
    print(user2,"+++++++++++++++############")
    user=Videos.objects.filter(id=id).first()
    link=user.link
    field=user.field
    pic=user.pic
    if Savevideo.objects.filter(link=link) and Savevideo.objects.filter(user_id=user2):
        msg="Video alrdy saved in Your Playlist"
        user1=Savevideo.objects.filter(user_id=user2.id)

        return render(request,"health/playlist.html",{"user1":user1,"msg":msg})
    user3=Savevideo.objects.create(link=link,field=field,user_id=user2,pic=pic)
    return redirect ("playlist",id=id)

def playlist(request,id=None):
    user1=User.objects.get(pk=request.session["id"])
    user2=UserMaster.objects.get(user_id=user1.id)
    user1=Savevideo.objects.filter(user_id=user2.id)
    msg="Video saved in Playlist"
    return render(request,"health/playlist.html",{"user1":user1,"msg":msg})

def delvideo(request,id):
    user1=User.objects.get(pk=request.session["id"])
    user2=UserMaster.objects.get(user_id=user1.id)
    row=Savevideo.objects.filter(id=id ,user_id=user2.id)
    print("--------------^^^^^^^^^^^^^^----------------------")
    row.delete()
    user1=User.objects.get(pk=request.session["id"])
    user2=UserMaster.objects.get(user_id=user1.id)
    user1=Savevideo.objects.filter(user_id=user2.id)
    msg="Video Removed From Your Playlist"
    return render(request,"health/playlist.html",{"user1":user1,"msg":msg})
def savedvideo(request,id=None):
    user1=User.objects.get(pk=request.session["id"])
    user2=UserMaster.objects.get(user_id=user1.id)
    user1=Savevideo.objects.filter(user_id=user2.id)
    return render(request,"health/playlist.html",{"user1":user1})




############################### Admin Views #####################################

def all_users(request):
  if "id" in request.session:
    users=UserModel.objects.all()
    print(users,"##################")
    return render(request, "health/all_users.html", {"users":users })
  return render(request,"health/login.html")

def add_user(request):
  if "id" in request.session:
    if request.method=="POST":
        
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        contact_no= request.POST['contact_no']
        email= request.POST['email']
        username=request.POST['username']
        password= request.POST['password']
        cpassword= request.POST['cpassword']
        Gender=request.POST['gender']

        user = User.objects.filter(email=email)

        if user:
            message="User Already Exists"
            return render(request, "health/add_user.html", {"msg":message})
        else:
            if password == cpassword:
                print(password,"#########################")
                password=make_password(password)
                user1=User.objects.create(password=password, email=email,first_name=first_name, last_name=last_name, username=username, is_staff=0,is_superuser=0, is_active=1, date_joined=datetime.now())
                user2=UserMaster.objects.create(user_id=user1,role="As a User")
                newuser=UserModel.objects.create(user_id=user2,contact_no=contact_no,Gender=Gender)
                return redirect("all_users")
            else:
                    message="password does not matches please check"
                    return render(request, "health/add_user.html", {"msg":message})
    return render(request, "health/add_user.html")
  return render(request,"health/login.html")
def delete_users(request, id):
  if "id" in request.session:
    user=User.objects.get(id=id)
    user.delete()
    return redirect("all_users")
  return render(request,"health/login.html")

def all_trainers(request):
   if "id" in request.session:
    users=TrainerModel.objects.all()
    print(users,"##################")
    return render(request, "health/all_trainers.html", {"users":users})
   return render(request,"health/login.html")
  
def add_trainers(request):
  if "id" in request.session:
    if request.method=="POST":
        Name=request.POST["name"]
        Age=request.POST["age"]
        contact_no=request.POST["contact"]
        Gender=request.POST["gender"]
        Fees=request.POST["fees"]
        Fees1=request.POST["fees1"]
        Fees2=request.POST["fees2"]
        Expertise=request.POST["expertise"]
        Experience=request.POST["experience"]
        profile=request.FILES.get("profile")
        TrainerModel.objects.create(Name=Name, Age=Age, contact_no=contact_no,Gender=Gender,Fees=Fees,Fees1=Fees1,Fees2=Fees2,Expertise=Expertise,Experience=Experience,profile=profile)
        return redirect("all_trainers")
    return render(request, "health/add_trainers.html")
  return render(request,"health/login.html")


def delete_trainers(request, id):
  if "id" in request.session:
    user=TrainerModel.objects.get(id=id)
    user.delete()
    return redirect("all_trainers")
  return render(request,"health/login.html")


def daily_food_items(request):
  if "id" in request.session:
    diet=intakediet.objects.all()
    return render(request, "health/daily_food_items.html", {"diet":diet })
  return render(request,"health/login.html")

def add_daily_food_items(request):
  if "id" in request.session:
 
    if request.method=="POST":
        food=request.POST["food"]
        print(request.POST.get("cal"),"$$$$$$$$$$$$$$$$$$$$")
        calorie=request.POST["cal"]
        veg_nonveg=request.POST["veg_nonveg"]
        intakediet.objects.create(intakefood=food, intakecalorie=calorie, veg_nonveg=veg_nonveg)
        return render(request, "health/messages.html",{"msg":"Food Added Succesfully"})
    return render(request, "health/add_daily_food_items.html")
  return render(request,"health/login.html")
def delete_daily_food_items(request,id):
  if "id" in request.session:
 
    diet=intakediet.objects.get(id=id)
    diet.delete()
    return redirect("daily_food_items")
  return render(request,"health/login.html")

def daily_breakfast_food(request):
   if "id" in request.session:
    diet=Breakfast.objects.all()
    return render(request, "health/daily_breakfast_food.html", {"diet":diet })
   return render(request,"health/login.html")

def add_daily_breakfast_food(request):
  if "id" in request.session:
    if request.method=="POST":
        food=request.POST["bfood"]
        print(request.POST.get("bcal"),"$$$$$$$$$$$$$$$$$$$$")
        calorie=request.POST["bcal"]
        veg_nonveg=request.POST["veg_nonveg"]
        Breakfast.objects.create(Breakfastfood=food, Breakfastcalorie=calorie, Bvn=veg_nonveg)
        return render(request, "health/messages.html",{"msg":"Food Added Succesfully"})
    return render(request, "health/add_daily_breakfast_food.html")
  return render(request,"health/login.html")
def delete_daily_breakfast_food(request,id):
  if "id" in request.session:
    diet=Breakfast.objects.get(id=id)
    
    diet.delete()
    return redirect("daily_breakfast_food")
  return render(request,"health/login.html")

def daily_lunch_food(request):
   if "id" in request.session:
    diet=Lunch.objects.all()
    return render(request, "health/daily_lunch_food.html", {"diet":diet })
   return render(request,"health/login.html")

def add_daily_lunch_food(request):
  if "id" in request.session:
    if request.method=="POST":
        food=request.POST["lfood"]
        print(request.POST.get("lcal"),"$$$$$$$$$$$$$$$$$$$$")
        calorie=request.POST["lcal"]
        veg_nonveg=request.POST["veg_nonveg"]
        Lunch.objects.create(Lunchfood=food, Lunchcalorie=calorie, Lvn=veg_nonveg)
        return render(request, "health/messages.html",{"msg":"Food Added Succesfully"})
    return render(request, "health/add_daily_lunch_food.html")
  return render(request,"health/login.html")
def delete_daily_lunch_food(request,id):
  if "id" in request.session:
    diet=Lunch.objects.get(id=id)
    diet.delete()
    return redirect("daily_lunch_food")
  return render(request,"health/login.html")

def daily_dinner_food(request):
  if "id" in request.session:
    diet=Dinner.objects.all()
    return render(request, "health/daily_dinner_food.html", {"diet":diet })
  return render(request,"health/login.html")

def add_daily_dinner_food(request):
  if "id" in request.session:
    if request.method=="POST":
        food=request.POST["dfood"]
        print(request.POST.get("dcal"),"$$$$$$$$$$$$$$$$$$$$")
        calorie=request.POST["dcal"]
        veg_nonveg=request.POST["veg_nonveg"]
        Dinner.objects.create(Dinnerfood=food, Dinnercalorie=calorie, Dvn=veg_nonveg)
        return render(request, "health/messages.html",{"msg":"Food Added Succesfully"})
    return render(request, "health/add_daily_dinner_food.html")
  return render(request,"health/login.html")
def delete_daily_dinner_food(request,id):
  if "id" in request.session:
    diet=Dinner.objects.get(id=id)
    diet.delete()
    return redirect("daily_dinner_food")
  return render(request,"health/login.html")


def wallet(request):
 if "id" in request.session:
  if request.session["id"] :
   user3=UserModel.objects.get(user_id=request.session["id"])
   if user3.Balance is None:
        balance=0
        try:
            wallet_details=WalletModel.objects.filter(user_id=request.session["id"]).all()
            amounts=[wallet.amount_transaction for wallet in wallet_details]
            balance=sum(amounts)
            user3.Balance=balance
            user3.save()
        except:
            pass
        return render(request,"health/wallet.html",{"balance":user3.Balance})
   else:
        balance=user3.Balance
        user3.Balance=balance
        user3.save()
        return render(request,"health/wallet.html",{"balance":user3.Balance})

  else:
        return redirect("/login")
 return render(request,"health/login.html")

def add_balance(request):
  if "id" in request.session:
    return render(request, "health/add_balance.html")
  return render(request,"health/login.html")
def balance_added(request):
  if "id" in request.session:
    user3=UserModel.objects.get(user_id=request.session["id"])
    current_user=User.objects.get(id=request.session["id"])
    amount_added=request.POST["balance"]
    wallet=WalletModel.objects.create(user_id=current_user,amount_transaction=amount_added,date=date.today(),time=datetime.now().time(),amount_type="Added to Wallet")
    balance=user3.Balance+float(amount_added)
    user3.Balance=balance
    user3.save()
    msg="Amount added Succesfully"
    expirydate=timezone.now()+timedelta(days=30)
    print(expirydate<timezone.now(),"^^^^^^^^^^^^^^^^^^^^^^^^^")
    return render(request,"health/add_balance.html",{"msg":msg,"amount_added":amount_added})
  return render(request,"health/login.html")   
   
def subscription(request):
  if "id" in request.session:
    user=UserModel.objects.get(user_id=request.session["id"])
    user1=User.objects.get(id=request.session["id"])
    if user.expirydate is None and user1.is_superuser==0:
      return render(request, "health/subscription.html")
    elif user.expirydate is not None and user1.is_superuser==0:
      return render(request,"health/home.html",{"expirydate":user.expirydate})
    else:
      return render(request,"health/home2.html")
  return render(request,"health/login.html")

def checkbalance(request,id):
  if "id" in request.session:
    user3=UserModel.objects.get(user_id=request.session["id"])
    option=request.POST["subscription"]
    wallet_details=WalletModel.objects.filter(user_id=id).all()
    # amounts=[wallet.amount_transaction for wallet in wallet_details]
    # balance=sum(amounts)
    # user3.Balance=balance
    # user3.save()

    # print(amounts)
    # print(balance,"----------------++++----------------")
    # print(option,"----------------------")
    if user3.Balance is not None:
    
     if user3.Balance<int(option) :
        msg="You dont have sufficent Balance please Add Money To your wallet"
        return render(request,"health/add_balance.html",{"msg":msg})
    
     elif user3.Balance>=float(option):
    #   expirydate=timezone.now()+timedelta(days=30)
    #   print(expirydate<timezone.now(),"^^^^^^^^^^^^^^^^^^^^^^^^^")
        if request.session["id"]:
             user3=UserModel.objects.get(user_id=request.session["id"])
             if request.session["id"]:
                user3=UserModel.objects.get(user_id=request.session["id"])
                balance=user3.Balance-float(option)
                user3.Balance=balance
                user3.save()
                if option=="199":
                  expirydate=timezone.now()+ timedelta(days=30)
                  user3.expirydate=expirydate
                  user3.save()
                
                if option=="350":
                  expirydate=timezone.now()+ timedelta(days=90)
                  user3.expirydate=expirydate
                  user3.save()
                if option=="999":
                  expirydate=timezone.now()+ timedelta(days=365)
                  user3.expirydate=expirydate
                  user3.save()

                return redirect("home")
    msg="You dont have sufficent Balance please Add Money To your wallet"
    return render(request,"health/add_balance.html",{"msg":msg})
  return render(request,"health/login.html")

def allvideos(request):
  if "id" in request.session:
    if request.session["id"]:
      videos1=Videos.objects.all()
      return render(request,"health/allvideos.html",{"videos":videos1})
    else:
      return render(request,"health/login.html")
  return render(request,"health/login.html")

def delete_videos(request,id):
  if "id" in request.session:
    video=Videos.objects.get(id=id)
    video.delete()
    return redirect("allvideos")
  return render(request,"health/login.html")

def add_videos(request):
  if "id" in request.session:
    if request.method=="POST":
        link=request.POST["link"]
        field=request.POST["field"]
        pic=request.FILES.get("thumbnail")
        Videos.objects.create(link=link, field=field, pic=pic)
        return render(request, "health/messages.html",{"msg":"Video Added Succesfully"})
    return render(request, "health/addvideos.html")
  return render(request,"health/login.html")

def water_amount(request):
    wat=WaterIntakeModel.objects.filter(user_id=request.session["id"])
    dat=[e.dat for e in wat]
    if len(dat)==0:
        pass
    else:
        d=dat[-1]
        if d==datetime.now().date():
            pass
        else:
            wat.delete()
    if request.POST.get('water') is None:
        wat=WaterIntakeModel.objects.filter(user_id=request.session["id"])
        wat_amount=[e.quantity for e in wat]
        if len(wat_amount) ==0:
            return render(request, "health/water.html",{"s":0})
        else:
            s=wat_amount[-1]
            return render(request, "health/water.html",{"s":s})

    if request.method=="POST":
        user_id=UserMaster.objects.get(id=request.session["id"])
        water=request.POST['water']
        water_val_per=int(water)*12.5
        s=request.POST["s"]
        print(s,"ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
        if s == "":
            s=None
        print(s,"ddddddddddddddddddddddddd")
        if s is None:
            print("pooooooooooooooooooooooooooooooo")
            s=water_val_per
            WaterIntakeModel.objects.create(Glass=water, quantity=s, user_id=user_id, dat=datetime.now().date())
        else:
            print("aajaaaaaaaaaaaaaaaaaaaa")
            s=float(s)
            print(s,"gggggggggggggggggggggggggg22222222222222gggggggggggggggggggggggggggggggggg")
            s+=water_val_per
            if s>100:
                return render(request, "health/water.html", {"msg":"Choose Glass Wisely","s":s-water_val_per})
            WaterIntakeModel.objects.create(Glass=water, quantity=s, user_id=user_id, dat=datetime.now().date())
            print(s,"gggggggggggggggggggggggggggggg4444444444444gggggggggggggggggggggggggggggggg")
        if s==100:
           return render(request, "health/water.html", {"msg":"Hurrah!! You have completed your todays Water Intake Target","s":100}) 
        if s>100:
            return render(request, "health/water.html", {"msg":"Choose Glass Wisely","s":s-water_val_per})
        return render(request, "health/water.html", {"s":s})
    return render(request, "health/water.html")


# 100 gm Wheat Upma 120 veg

