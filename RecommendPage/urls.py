from django.urls import path
from RecommendPage import views

app_name = 'RecommendPage'  # Define the namespace for the app

urlpatterns = [
    path('recommend/',views.recommend,name='recommend'),
    #path('',views.logout_user,name='logout_user')
]