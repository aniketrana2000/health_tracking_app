from django.db import models
from django.contrib.auth.models import User

class UserMaster(models.Model):
    user_id=models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.CharField(max_length=50)

class UserModel(models.Model):
    user_id=models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    contact_no= models.CharField(max_length=50)
    Age=models.IntegerField(null=True)
    Height=models.IntegerField(null=True)
    Weight=models.IntegerField(null=True)
    Gender=models.CharField(max_length=50)
    vegnonveg=models.CharField(max_length=50)
    goalweight=models.IntegerField(null=True)
    Balance=models.FloatField(null=True)
    expirydate=models.DateTimeField(null=True)

class WalletModel(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    amount_type = models.CharField(max_length=50)
    date = models.DateField()
    time=models.TimeField()
    amount_transaction=models.FloatField()
    duration=models.CharField(max_length=100,null=True)

# class Trainer(models.Model):
#     user_id=models.ForeignKey(UserMaster, on_delete=models.CASCADE)
#     contact_no= models.CharField(max_length=50)
#     Gender=models.CharField(max_length=50)
#     Age=models.IntegerField(null=True)
#     # Expertise=models.CharField(max_length=100)
#     # Experience=models.IntegerField(null=True)
#     # Name=models.CharField(max_length=100)
#     # Fees=models.IntegerField(null=True)
class Breakfast(models.Model):
    Breakfastfood= models.CharField(max_length=50)
    Breakfastcalorie=models.IntegerField(null=True)
    Bvn=models.CharField(max_length=50)

class Lunch(models.Model):
    Lunchfood= models.CharField(max_length=50)
    Lunchcalorie=models.IntegerField(null=True)
    Lvn=models.CharField(max_length=50)

class Dinner(models.Model):
    Dinnerfood= models.CharField(max_length=50)
    Dinnercalorie=models.IntegerField(null=True)
    Dvn=models.CharField(max_length=50)



class intakediet(models.Model):
    intakefood = models.CharField(max_length=200)
    intakecalorie= models.IntegerField(null=True)
    veg_nonveg=models.CharField(max_length=200)

class UserIntakeModel(models.Model):
    user_id=models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    food = models.CharField(max_length=200)
    calorie= models.IntegerField(null=True)

class WaterIntakeModel(models.Model):
    user_id=models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    Glass= models.IntegerField(null=True)
    quantity= models.FloatField(null=True)
    dat=models.DateField(null=True)

class TrainerModel(models.Model):
    contact_no= models.CharField(max_length=50)
    contact=models.CharField(max_length=100,null=True)
    Gender=models.CharField(max_length=50)
    Age=models.IntegerField(null=True)
    Expertise=models.CharField(max_length=100)
    Experience=models.IntegerField(null=True)
    Name=models.CharField(max_length=100)
    Fees=models.IntegerField(null=True)
    Fees1=models.IntegerField(null=True)
    Fees2=models.IntegerField(null=True)
    profile=models.ImageField(upload_to="static/health/image")
    profile1=models.ImageField(blank=True)
    
class Videos(models.Model):
    link= models.URLField(max_length=800) # add link here
    field=models.CharField(max_length=80)  # Gain Loss
    pic=models.ImageField(upload_to="static/health/image",null=True)

class Savevideo(models.Model):
    user_id=models.ForeignKey(UserMaster, on_delete=models.CASCADE )
    link = models.URLField(max_length=500,null=True)
    pic=models.ImageField(upload_to="static/health/image",null=True)
    field= models.CharField(max_length=80,null=True)



