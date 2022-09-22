from django.contrib import admin
from django.urls import path
from health import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('', views.RegisterUser, name="register"),
    path('loginuser/', views.LoginUser, name="login"),
    path('logoutuser/', views.logout, name="logout"),
    path('profile/<int:pk>/', views.ProfilePage, name="profile"),
    path('updateprofile/<int:pk>/', views.UpdateProfile, name="updateprofile"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('bmi/<int:pk>/', views.bmi, name="bmi"),
    path('goalbmi/<int:pk>/', views.goalbmi, name="goalbmi"),
    path('diet/<str:AIM_BMR>/<int:pk>/', views.diet, name="diet"),
    path('foodlist/<int:l1>/', views.foodlist, name="foodlist"),
    path('foodlist/<int:l1>/<int:s>', views.foodlist, name="foodlist"),
    path('foodlist/', views.foodlist, name="foodlist"),

    path('delete_diet/', views.delete_diet, name="delete_diet"),
    path('water/', views.water, name="water"),
    path('all_users/', views.all_users, name="all_users"),
    path('add_user/', views.add_user, name="add_user"),
    path('delete_users/<int:id>/', views.delete_users, name="delete_users"),
    path('all_trainers/', views.all_trainers, name="all_trainers"),
    path('view_profile/<int:id>/', views.view_profile, name="view_profile"),
    path('add_trainers/', views.add_trainers, name="add_trainers"),
    path('delete_trainers/<int:id>/', views.delete_trainers, name="delete_trainers"),
    path('Videos1/', views.Videos1, name="Videos1"),
    path('savevideo/<int:id>', views.savevideo, name="savevideo"),
    path('delvideo/<int:id>/', views.delvideo, name="delvideo"),
    path('savedvideo/', views.savedvideo, name="savedvideo"),
    path('playlist/<int:id>', views.playlist, name="playlist"),
    path('daily_food_items/', views.daily_food_items, name="daily_food_items"),
    path('delete_daily_food_items/<int:id>', views.delete_daily_food_items, name="delete_daily_food_items"),
    path('add_daily_food_items/', views.add_daily_food_items, name="add_daily_food_items"),
    path('daily_breakfast_food/', views.daily_breakfast_food, name="daily_breakfast_food"),
    path('delete_daily_breakfast_food/<int:id>', views.delete_daily_breakfast_food, name="delete_daily_breakfast_food"),
    path('add_daily_breakfast_food/', views.add_daily_breakfast_food, name="add_daily_breakfast_food"),
    path('daily_lunch_food/', views.daily_lunch_food, name="daily_lunch_food"),
    path('delete_daily_lunch_food/<int:id>', views.delete_daily_lunch_food, name="delete_daily_lunch_food"),
    path('add_daily_lunch_food/', views.add_daily_lunch_food, name="add_daily_lunch_food"),
    path('daily_dinner_food/', views.daily_dinner_food, name="daily_dinner_food"),
    path('delete_daily_dinner_food/<int:id>', views.delete_daily_dinner_food, name="delete_daily_dinner_food"),
    path('add_daily_dinner_food/', views.add_daily_dinner_food, name="add_daily_dinner_food"),
    path('wallet/', views.wallet, name="wallet"),
    path('add_balance/', views.add_balance, name="add_balance"),
    path('balance_added/', views.balance_added, name="balance_added"),
    path('subscription/', views.subscription, name="subscription"),
    path('checkbalance/<int:id>', views.checkbalance, name="checkbalance"),
    path('Trainerlist/', views.Trainerlist, name="Trainerlist"),
    path('allvideos/', views.allvideos, name="allvideos"),
    path('add_videos/', views.add_videos, name="add_videos"),
    path('delete_videos/<int:id>/', views.delete_videos, name="delete_videos"),
    path('water_amount/', views.water_amount, name="water_amount")

    # path('register/', views.register, name="register"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
