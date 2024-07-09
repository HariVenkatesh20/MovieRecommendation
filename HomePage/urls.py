from django.urls import path
from HomePage import views


urlpatterns = [
    path('',views.mainhome,name='mainhome'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login_user'),
    path('register/',views.register_user,name='register_user'),
    path('logout/',views.logout_user,name='logout_user'),
    path('search/',views.search_bar,name='search_bar'),
    path('suggest_movies/', views.suggest_movies, name='suggest_movies'),

]