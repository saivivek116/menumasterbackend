from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

MOCKED_RESTAURANTS = [
    {
        "id": 1,
        "name": "Spice Delight",
        "cuisine": "Indian",
        "location": "12 Curry Lane",
        "rating": 4.8,
        "menu": {
            "appetisers": [
                {"name": "Samosa", "price": 5},
                {"name": "Paneer Tikka", "price": 8},
            ],
            "salads": [
                {"name": "Kachumber Salad", "price": 6},
                {"name": "Chana Chaat", "price": 7},
            ],
            "maincourses": [
                {"name": "Butter Chicken", "price": 15},
                {"name": "Paneer Butter Masala", "price": 13},
            ]
        }
    },
    {
        "id": 2,
        "name": "Mumbai Masala",
        "cuisine": "Indian",
        "location": "34 Spice Road",
        "rating": 4.7,
        "menu": {
            "appetisers": [
                {"name": "Pani Puri", "price": 4},
                {"name": "Aloo Tikki", "price": 6},
            ],
            "salads": [
                {"name": "Green Salad", "price": 5},
                {"name": "Fruit Chaat", "price": 8},
            ],
            "maincourses": [
                {"name": "Rogan Josh", "price": 17},
                {"name": "Dal Makhani", "price": 12},
            ]
        }
    },
    {
        "id": 3,
        "name": "The American Diner",
        "cuisine": "American",
        "location": "56 Liberty Ave",
        "rating": 4.6,
        "menu": {
            "appetisers": [
                {"name": "Buffalo Wings", "price": 10},
                {"name": "Mozzarella Sticks", "price": 7},
            ],
            "salads": [
                {"name": "Caesar Salad", "price": 9},
                {"name": "Coleslaw", "price": 5},
            ],
            "maincourses": [
                {"name": "Cheeseburger", "price": 12},
                {"name": "BBQ Ribs", "price": 18},
            ]
        }
    },
    {
        "id": 4,
        "name": "Desi Dhaba",
        "cuisine": "Indian",
        "location": "78 Punjab Street",
        "rating": 4.5,
        "menu": {
            "appetisers": [
                {"name": "Pakoras", "price": 6},
                {"name": "Dahi Puri", "price": 7},
            ],
            "salads": [
                {"name": "Aloo Chaat", "price": 8},
                {"name": "Onion Salad", "price": 4},
            ],
            "maincourses": [
                {"name": "Chicken Biryani", "price": 14},
                {"name": "Saag Paneer", "price": 13},
            ]
        }
    },
    {
        "id": 5,
        "name": "Burger Palace",
        "cuisine": "American",
        "location": "91 Burger Blvd",
        "rating": 4.7,
        "menu": {
            "appetisers": [
                {"name": "Onion Rings", "price": 5},
                {"name": "Chicken Nuggets", "price": 8},
            ],
            "salads": [
                {"name": "Garden Salad", "price": 6},
                {"name": "Potato Salad", "price": 7},
            ],
            "maincourses": [
                {"name": "Double Cheeseburger", "price": 14},
                {"name": "Grilled Chicken Sandwich", "price": 12},
            ]
        }
    },
    {
        "id": 6,
        "name": "Curry House",
        "cuisine": "Indian",
        "location": "123 Spice Alley",
        "rating": 4.9,
        "menu": {
            "appetisers": [
                {"name": "Tandoori Chicken", "price": 9},
                {"name": "Lamb Seekh Kebab", "price": 12},
            ],
            "salads": [
                {"name": "Mixed Veg Salad", "price": 5},
                {"name": "Papdi Chaat", "price": 7},
            ],
            "maincourses": [
                {"name": "Chicken Tikka Masala", "price": 16},
                {"name": "Lamb Rogan Josh", "price": 18},
            ]
        }
    },
    {
        "id": 7,
        "name": "BBQ Nation",
        "cuisine": "American",
        "location": "25 Grill Street",
        "rating": 4.8,
        "menu": {
            "appetisers": [
                {"name": "BBQ Chicken Wings", "price": 11},
                {"name": "Fried Shrimp", "price": 12},
            ],
            "salads": [
                {"name": "Wedge Salad", "price": 8},
                {"name": "Pasta Salad", "price": 7},
            ],
            "maincourses": [
                {"name": "BBQ Pulled Pork", "price": 17},
                {"name": "Grilled Steak", "price": 22},
            ]
        }
    },
    {
        "id": 8,
        "name": "Tandoori Flames",
        "cuisine": "Indian",
        "location": "67 Curry Circle",
        "rating": 4.6,
        "menu": {
            "appetisers": [
                {"name": "Vegetable Samosa", "price": 4},
                {"name": "Chicken Kebab", "price": 9},
            ],
            "salads": [
                {"name": "Cucumber Raita", "price": 4},
                {"name": "Mint Chutney Salad", "price": 5},
            ],
            "maincourses": [
                {"name": "Lamb Vindaloo", "price": 17},
                {"name": "Fish Curry", "price": 15},
            ]
        }
    },
    {
        "id": 9,
        "name": "Grill Master",
        "cuisine": "American",
        "location": "39 BBQ Lane",
        "rating": 4.7,
        "menu": {
            "appetisers": [
                {"name": "BBQ Nachos", "price": 8},
                {"name": "Jalapeno Poppers", "price": 7},
            ],
            "salads": [
                {"name": "Greek Salad", "price": 9},
                {"name": "Spinach Salad", "price": 8},
            ],
            "maincourses": [
                {"name": "BBQ Brisket", "price": 20},
                {"name": "Grilled Salmon", "price": 19},
            ]
        }
    },
    {
        "id": 10,
        "name": "Royal Curry",
        "cuisine": "Indian",
        "location": "85 King Street",
        "rating": 4.9,
        "menu": {
            "appetisers": [
                {"name": "Paneer Pakora", "price": 8},
                {"name": "Chicken Tikka", "price": 10},
            ],
            "salads": [
                {"name": "Tomato and Onion Salad", "price": 6},
                {"name": "Corn Chaat", "price": 7},
            ],
            "maincourses": [
                {"name": "Mutton Curry", "price": 18},
                {"name": "Palak Paneer", "price": 14},
            ]
        }
    }
]

# class RestaurantListView(APIView):
#     def get(self, request):
#         return Response(RESTAURANTS)


# class RestaurantMenuView(APIView):
#     def get(self, request, restaurant_id):
#         menu = MENUS.get(restaurant_id)
#         if menu:
#             restaurant = next((r for r in RESTAURANTS if r['id'] == restaurant_id), None)
#             if restaurant:
#                 return Response({
#                     "id": restaurant['id'],
#                     "name": restaurant['name'],
#                     "categories": menu['categories']
#                 })
#         return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def getRestaurants(request):
    restarurants = []
    for res in MOCKED_RESTAURANTS:
        restarurants.append({
            "id": res['id'],
            "name": res['name'],
            "cuisine": res['cuisine'],
            "rating": res['rating'],
        })
    return Response(restarurants)

@api_view(['GET'])
def getRestaurantMenu(request, restaurant_id):
    restaurant = next((r for r in MOCKED_RESTAURANTS if r['id'] == restaurant_id), None)
    if restaurant:
        return Response(restaurant['menu'])
    return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)


def index(request):
    return HttpResponse("Hello, world.")

