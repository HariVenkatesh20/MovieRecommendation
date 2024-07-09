from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd
import os
from django.http import JsonResponse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from .forms import LoginForm,RegisterForm
#from .models import UserRegister




# Create your views here.

def mainhome(request):
    return render(request,'Home.html')


def search_bar(request): 
    if 'q' in request.GET:
        query = request.GET['q']
        try:

            csv_path = os.path.abspath('movies_data.csv')  # Replace 'path/to/movies.csv' with the actual path

            if not os.path.exists(csv_path):
                raise FileNotFoundError("Movie dataset not found. Please make sure the CSV file exists.")

            movies_df = pd.read_csv(csv_path)
            movies_df.dropna(subset=['title'], inplace=True)


            matched_movies = movies_df[movies_df['title'].str.contains(query, case=False)]
            #matched_movies = movies_df[movies_df['title'].str.lower() == query.lower()]


            if not matched_movies.empty:
                matched_movie_details = matched_movies.to_dict(orient='records')
            else:
                matched_movie_details = []    

            # Compute recommendations for the searched movie
            tfidf_vectorizer = TfidfVectorizer(stop_words='english')
            movies_df['genres'] = movies_df['genres'].fillna('')
            tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['genres'])
            cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
            recommended_movies_details = get_recommendations(query,movies_df,cosine_sim=cosine_sim)
            #if recommend_movies_details is  None:
                # Handle the case where no recommendations are found
                #recommend_movies_details = pd.DataFrame()            
            '''matched_movie_details = matched_movie_details if matched_movie_details else []
             recommended_movies_details = recommended_movies_details.tolist() if isinstance(recommended_movies_details, pd.Series) else []'''
            if not recommended_movies_details.empty:
                #query_genre = matched_movies.iloc[0]['genres']  # Get genres of the searched movie
                recommended_movies_details = recommended_movies_details[recommended_movies_details['genres'].str.contains(query)]
            else:
                recommend_movies_details = pd.DataFrame()           

            # Store matched movie details and recommended movies in the session
            request.session['matched_movies'] = matched_movie_details
            request.session['recommended_movies'] = recommended_movies_details.to_dict(orient='records') if not recommended_movies_details.empty else []
                
            # Redirect to the recommend page
            return redirect(reverse('RecommendPage:recommend'))
            
            #return redirect('RecommendPage:recommend', matched_movies=matched_movie_details)
        except BrokenPipeError as e:
            # Handle BrokenPipeError gracefully
            messages.error(request, "Connection closed by client. Please try again.")
    else:
        print("'q' parameter not found in request.GET")        
    return render(request, 'Home.html')   

# View for movie suggestions
'''def suggest_movies(request):
    query = request.GET.get('q', '')
    suggestions = []

    if len(query) >= 2:
        # Assuming you have a DataFrame named 'movies_df' with movie titles
        matched_movies = movies_df[movies_df['title'].str.contains(query, case=False)]
        suggestions = matched_movies['title'].tolist()

    return JsonResponse({'suggestions': suggestions})'''

def suggest_movies(request,movies_df):
    query = request.GET.get('q', '')
    if len(query) == 1:
        movies = movies_df.objects.filter(title__istartswith=query)
        return render(request, 'Home.html', {'movies': movies})
    return render(request, 'Home.html', {'movies': []})  


def get_recommendations(query, movie_df,cosine_sim):
    if query not in movie_df['title']:
        print('Movie not found in dataset:', query)
        return pd.DataFrame()
    idx = movie_df[movie_df['title'] == query].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  
    movie_indices = [i[0] for i in sim_scores]
    return movie_df.iloc[movie_indices]
    #recommended_movies = movie_df.iloc[movie_indices]
    
    # Print details of recommended movies
    '''for  index,movie in recommended_movies.iterrows():
        print("Title:", movie['title'])
        print("Genres:", movie['genres'])
        print()'''




'''def registration_view(request):
    if request.method == 'POST':
        if 'registerbt' in request.POST:
            rform = UserForm(request.POST)
            if rform.is_valid():
                rform.save()
                return redirect("register_view")
        
        elif 'loginbt' in request.POST:
            lform = LoginForm(request.POST)
            username = request.POST['mail']
            password = request.POST['passw']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('mainhome')
            else:
                messages.success(request, "Incorrect Password/Userid , Try Again..")
                return redirect('mainhome')

    else:
        form = UserForm()
    return render(request,'register.html',{'form':form})'''


def login_user(request):  
    if request.method == 'POST':           
        lform = LoginForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('mainhome')
        else:
            pass
            #return render(request,'Home.html')
    return render(request,'Login.html')


def register_user(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user =authenticate(username=username,password=password)
            login(request,user)
            return redirect('mainhome')
    else:
        form=RegisterForm()
        
    return render(request, 'register.html',{'form':form})



def about(request):
    return render(request,'about.html')




@login_required
def logout_user(request):
    logout(request)
    return redirect('mainhome')