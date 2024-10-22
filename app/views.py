from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CafeResturant, Dish, Team, Reviews
from datetime import datetime
from django.contrib import messages
from adminapp.models import User
import uuid
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import make_password

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == 'POST':
        data = request.POST
        email = data['email']
        password = data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request,"Successfully Login!")
            return redirect("index")
        else:
            messages.warning(request,"Incorrect email or password!")
    return render(request,'user_login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        password2 = data.get('password2')
        email_check = User.objects.filter(email=email)
        if not email_check.exists():
            if password == password2:
                uid = uuid.uuid1()
                hashed_password = make_password(password)
                User.objects.create(email=email, first_name=first_name,last_name=last_name, password=hashed_password, uid=uid)
                messages.success(request,"Successfully SignUp!")
                return redirect('index')
            else:
                messages.warning(request,"Password does not match!")
                return redirect('signup')
        else:
            messages.warning(request,"Email already exists!")
            return redirect('signup')
    return render(request, 'signup.html')

@login_required()
def user_change_password(request):
    if request.method == "POST":
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        user = User.objects.get(uid=request.user.uid)
        print(user.first_name)
        if p1 == p2:
            user.set_password(p1) 
            user.save()   
            messages.success(request,"Successfully Change Password!")
            return redirect('index')
        else:
            messages.warning(request,"Password does not match!")
            return redirect('user_change_password')
    return render(request, 'user_change_password.html')

@login_required()
def user_logout(request):
    try:
        logout(request)
        messages.success(request, 'Logout Successfully!')
        return redirect('index')
    except:
            messages.warning(request, 'Request is not responed please check your internet connection and try again!')
            return redirect('index')

def index(request):
    try:
        cafe_reviews = Reviews.objects.filter(rating__gt=3).order_by('?')[:6]
        return render(request, 'index.html', {'active' : 'active', 'cafe_reviews' : cafe_reviews})
    except:
            messages.warning(request, 'Request is not responed please check your internet connection and try again!')
            return redirect('index')

def cafe(request):
    try:
        time_str = datetime.now().strftime('%H:%M:%S')  
        time_format = '%H:%M:%S'
        time_datetime = datetime.strptime(time_str, time_format)
        time_now = time_datetime.time()

        cafes = CafeResturant.objects.filter(type_of='cafe')
        famous_cafes = CafeResturant.objects.all()[:3]
        return render(request, 'cafe.html', {'active2' : 'active', 'cafes' : cafes, 'famous_cafes' : famous_cafes, 'time_now' : time_now})
    except:
            messages.warning(request, 'Request is not responed please check your internet connection and try again!')
            return redirect('index')

def cafe_detail(request, id):
    try:
        time_str = datetime.now().strftime('%H:%M:%S')  
        time_format = '%H:%M:%S'
        time_datetime = datetime.strptime(time_str, time_format)
        time_now = time_datetime.time()

        cafes = CafeResturant.objects.filter(type_of='cafe')
        caf = CafeResturant.objects.get(id=id)
        bf_dishes = Dish.objects.filter(cafe=caf, meal_name="breakfast")
        lunch_dishes = Dish.objects.filter(cafe=caf, meal_name="lunch")
        dinner_dishes = Dish.objects.filter(cafe=caf, meal_name="dinner")
        cafe_reviews = Reviews.objects.filter(cafe=caf).order_by('-rating')[:6]

        if request.method == "POST" : 
            n1 = request.user.first_name
            n2 = request.user.last_name
            customer = n1 + ' ' + n2
            data = request.POST
            cafe_id = data.get('feedback-cafe')
            rating = data.get('rating')
            comment = data.get('comment')
            review_cafe = CafeResturant.objects.get(id=cafe_id)
            if rating:
                Reviews.objects.create(cafe=review_cafe, customer=customer, rating=rating, comment=comment)
                messages.success(request,"Thank you for your feedback!")
                return redirect(f'/cafe_detail/{review_cafe.id}')
            else:
                messages.warning(request,"Please Rate Us!")
                return redirect(f'/cafe_detail/{review_cafe.id}')

        return render(request, 'cafe_detail.html', {'active2' : 'active', 'cafes' : cafes, 'caf' : caf, 'bf_dishes' : bf_dishes, 'lunch_dishes' : lunch_dishes, 'dinner_dishes' : dinner_dishes, 'time_now' : time_now, 'cafe_reviews' : cafe_reviews})
    except:
            messages.warning(request, 'Request is not responed please check your internet connection and try again!')
            return redirect('/cafe/')

def restaurant(request):
    try:
        time_str = datetime.now().strftime('%H:%M:%S')  
        time_format = '%H:%M:%S'
        time_datetime = datetime.strptime(time_str, time_format)
        time_now = time_datetime.time()

        rest_ob = CafeResturant.objects.filter(type_of='resturant').order_by('-id')
        rest_famous = CafeResturant.objects.filter(type_of='resturant')[:3]
        return render(request, 'restaurant.html', {'active3' : 'active', 'rest_ob' : rest_ob, 'rest_famous' : rest_famous, 'time_now' : time_now})
    except:
            messages.warning(request, 'Request is not responed please check your internet connection and try again!')
            return redirect('index')

def restaurant_detail(request,id):
    try:
        time_str = datetime.now().strftime('%H:%M:%S')  
        time_format = '%H:%M:%S'
        time_datetime = datetime.strptime(time_str, time_format)
        time_now = time_datetime.time()

        rests = CafeResturant.objects.filter(type_of='resturant')
        rest = CafeResturant.objects.get(id=id)
        bf_dishes = Dish.objects.filter(cafe=rest, meal_name="breakfast")
        lunch_dishes = Dish.objects.filter(cafe=rest, meal_name="lunch")
        dinner_dishes = Dish.objects.filter(cafe=rest, meal_name="dinner")
        cafe_reviews = Reviews.objects.filter(cafe=rest).order_by('-rating')[:6]

        if request.method == "POST" : 
            n1 = request.user.first_name
            n2 = request.user.last_name
            customer = n1 + ' ' + n2
            data = request.POST
            cafe_id = data.get('feedback-cafe')
            
            rating = data.get('rating')
            comment = data.get('comment')
            review_cafe = CafeResturant.objects.get(id=cafe_id)
            if rating:
                Reviews.objects.create(cafe=review_cafe, customer=customer, rating=rating, comment=comment)
                messages.success(request,"Thank you for your feedback!")
                return redirect(f'/restaurant_detail/{review_cafe.id}')
            else:
                messages.warning(request,"Please Rate Us!")
                return redirect(f'/restaurant_detail/{review_cafe.id}')
            
        return render(request, 'restaurant_detail.html', {'active3' : 'active', 'bf_dishes' : bf_dishes, 'lunch_dishes' : lunch_dishes, 'dinner_dishes' : dinner_dishes, 'rests' : rests, 'rest' : rest, 'time_now' : time_now, 'cafe_reviews' : cafe_reviews})
    except:
            messages.warning(request, 'Request is not responed please check your internet connection and try again!')
            return redirect('/restaurant/')

def team(request):
    try:
        members = Team.objects.all()
        return render(request, 'team.html', {'active4' : 'active', 'members' : members})
    except:
            messages.warning(request, 'Request is not responed please check your internet connection and try again!')
            return redirect('index')

def about(request):
    try:
        return render(request, 'about.html')
    except:
            messages.warning(request, 'Request is not responed please check your internet connection and try again!')
            return redirect('index')

def search_bar(request):
    try:
        if request.method == 'POST':
            search = request.POST.get('search')
            caf = CafeResturant.objects.filter(cafe_name=search).first()
            if caf:
                if caf.type_of == 'cafe':
                    return redirect(f'/cafe_detail/{caf.id}')
                elif caf.type_of == 'resturant':
                    return redirect(f'/restaurant_detail/{caf.id}')
            else:
                messages.error(request, 'Not found, please enter correct name!')
                return redirect('index')
    except:
            messages.warning(request, 'Request is not responed please check your internet connection and try again!')
            return redirect('index')


    