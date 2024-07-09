
'''def get_recommendations(query, movie_df,cosine_sim):
    print(query)
    print(movie_df['title'].values)
    if query not in movie_df['title'].values:
        return None
    idx = movie_df[movie_df['title'] == query].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  
    movie_indices = [i[0] for i in sim_scores]
    return movie_df['title'].iloc[movie_indices]'''




