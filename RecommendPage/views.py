from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd 

# Create your views here.


def recommend(request):
    matched_movie_details = request.session.get('matched_movies', [])
    recommend_movies_details = request.session.get('recommend_movies', [])
    #print(matched_movie_details)
    print(recommend_movies_details)    
    if matched_movie_details:
        # Clear the session data after retrieving it
        request.session.pop('matched_movies', None)
        
        # Check if recommendations exist
        if recommend_movies_details:
            # Clear the session data for recommendations
            request.session.pop('recommend_movies', None)
            return render(request, 'recommend.html', {'matched_movies': matched_movie_details, 'recommend_movies': recommend_movies_details})
        else:
            return render(request, 'recommend.html', {'matched_movies': matched_movie_details, 'recommend_movies': []})
    else:
        return render(request, 'recommend.html', {'message': "No matched movies found."})



