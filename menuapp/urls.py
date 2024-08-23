from django.urls import path

from . import views
# from .views import RestaurantListView, RestaurantMenuView


urlpatterns = [
    path("", views.index, name="index"),
    # path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    # path('restaurants/<int:restaurant_id>/menu/', RestaurantMenuView.as_view(), name='restaurant-menu'),
    path("restaurants/", views.getRestaurants, name="restaurant-list"),
    path("restaurants/<int:restaurant_id>/menu/", views.getRestaurantMenu, name="restaurant-menu"),
]