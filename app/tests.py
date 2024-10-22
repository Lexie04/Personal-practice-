from django.test import TestCase
from datetime import datetime, timedelta
from .models import CafeResturant, Dish, Team, Reviews
from adminapp.models import User
import uuid
from django.contrib.auth.hashers import make_password
# Create your tests here.
class UsertestMethod(TestCase):
    def test_create_user(self):
        uid = uuid.uuid1()
        email = 'martin@gmail.com'     # this field is set to unique so give unique email whenever you try to add a new user.
        username = 'Martin Guptil'
        first_name = 'Martin'
        last_name = 'Guptil'
        password = '123'
        hashed_password = make_password(password)

        user = User.objects.create(email=email, username=username, first_name=first_name, last_name=last_name, password=hashed_password, uid=uid)

        self.assertEqual(user.uid, uid)
        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

class CafeTestMethod(TestCase):

    def test_create_cafe(self):
        time_str = datetime.now().strftime('%H:%M:%S')
        time_format = '%H:%M:%S'
        time_datetime = datetime.strptime(time_str, time_format)
        time_now = time_datetime.time()
        # Create a timedelta representing 6 hours
        six_hours = timedelta(hours=6)

        # Add the timedelta to time_now
        new_time = (datetime.combine(datetime.today(), time_now) + six_hours).time()

        cafe_name = 'Starbucks'      # this field is set to unique so give unique name whenever you try to add a new cafe.
        image = '/media/cafe/slider/pexels-lisa-fotios-1137745.jpg'
        type_of = 'cafe'
        location = 'East'
        description = 'Experience a blend of tradition and innovation. Our carefully curated menu pays homage to timeless classics, creating a haven for coffee enthusiasts.'
        contact_number = '+45 3378 334522'
        opening_time = time_now
        closing_time = new_time

        cafe = CafeResturant.objects.create(cafe_name=cafe_name, image=image, type_of=type_of, location=location, description=description, contact_number=contact_number, opening_time=opening_time, closing_time=closing_time)

        self.assertEqual(cafe.cafe_name, cafe_name)
        self.assertEqual(cafe.image, image)
        self.assertEqual(cafe.type_of, type_of)
        self.assertEqual(cafe.location, location)
        self.assertEqual(cafe.description, description)
        self.assertEqual(cafe.contact_number, contact_number)
        self.assertEqual(cafe.opening_time, opening_time)
        self.assertEqual(cafe.closing_time, closing_time)

    def test_create_restaurant(self):
        time_str = datetime.now().strftime('%H:%M:%S')
        time_format = '%H:%M:%S'
        time_datetime = datetime.strptime(time_str, time_format)
        time_now = time_datetime.time()
        # Create a timedelta representing 6 hours
        six_hours = timedelta(hours=6)

        # Add the timedelta to time_now
        new_time = (datetime.combine(datetime.today(), time_now) + six_hours).time()

        restaurant_name = 'Heritage'      # this field is set to unique so give unique name whenever you try to add a new restaurant.
        image = '/media/cafe/slider/pexels-lisa-fotios-1137745.jpg'
        type_of = 'resturant'
        location = 'East'
        description = 'Experience a blend of tradition and innovation. Our carefully curated menu pays homage to timeless classics, creating a haven for coffee enthusiasts.'
        contact_number = '+45 3378 334522'
        opening_time = time_now
        closing_time = new_time

        restaurant = CafeResturant.objects.create(cafe_name=restaurant_name, image=image, type_of=type_of, location=location, description=description, contact_number=contact_number, opening_time=opening_time, closing_time=closing_time)

        self.assertEqual(restaurant.cafe_name, restaurant_name)
        self.assertEqual(restaurant.image, image)
        self.assertEqual(restaurant.type_of, type_of)
        self.assertEqual(restaurant.location, location)
        self.assertEqual(restaurant.description, description)
        self.assertEqual(restaurant.contact_number, contact_number)
        self.assertEqual(restaurant.opening_time, opening_time)
        self.assertEqual(restaurant.closing_time, closing_time)

    def test_create_dish(self):
        cafe = CafeResturant.objects.create(cafe_name='London cafe', image='/media/cafe/slider/pexels-lisa-fotios-1137745.jpg', type_of='cafe', location='West', opening_time=datetime.now().time(), closing_time=(datetime.now() + timedelta(hours=6)).time())
        dish_name ='burger'
        ingredients = 'bread, souce, ketchup'
        meal_name = 'lunch'
        image = '/media/cafe/slider/pexels-lisa-fotios-1137745.jpg'
        price = 10

        dish = Dish.objects.create(cafe=cafe, image=image, dish_name=dish_name, meal_name=meal_name, price=price, ingredients=ingredients)

        self.assertEqual(dish.cafe, cafe)
        self.assertEqual(dish.dish_name, dish_name)
        self.assertEqual(dish.ingredients, ingredients)
        self.assertEqual(dish.meal_name, meal_name)
        self.assertEqual(dish.image, image)
        self.assertEqual(dish.price, price)

    def test_create_team(self):
        cafe = CafeResturant.objects.create(cafe_name='KFC', image='/media/cafe/slider/pexels-lisa-fotios-1137745.jpg', type_of='cafe', location='West', opening_time=datetime.now().time(), closing_time=(datetime.now() + timedelta(hours=6)).time())
        name = 'jhon'
        image = '/media/cafe/slider/pexels-lisa-fotios-1137745.jpg'
        post = 'waiter'
        description = 'responsible for deleiver meals.'

        team = Team.objects.create(cafe=cafe, image=image, name=name, post=post, description=description)

        self.assertEqual(team.cafe, cafe)
        self.assertEqual(team.image, image)
        self.assertEqual(team.name, name)
        self.assertEqual(team.post, post)
        self.assertEqual(team.description, description)

    def test_create_reviews(self):
        cafe = CafeResturant.objects.create(cafe_name='Burger King', image='/media/cafe/slider/pexels-lisa-fotios-1137745.jpg', type_of='cafe', location='West', opening_time=datetime.now().time(), closing_time=(datetime.now() + timedelta(hours=6)).time())
        customer = 'Morgen'
        rating = 4
        comment = 'Good taste.'

        review = Reviews.objects.create(cafe=cafe, customer=customer, rating=rating, comment=comment)

        self.assertEqual(review.cafe, cafe)
        self.assertEqual(review.customer, customer)
        self.assertEqual(review.rating, rating)
        self.assertEqual(review.comment, comment)

# Create your tests here.
