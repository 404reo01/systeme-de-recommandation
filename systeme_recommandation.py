import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('movies.csv')
credits = pd.read_csv('credits.csv')

# Remplacer les valeurs NaN dans la colonne 'overview' par une chaîne vide
movies['overview'] = movies['overview'].fillna("")

tfidf = TfidfVectorizer(stop_words='english')                
tfidf_matrix = tfidf.fit_transform(movies['overview'])      





similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)




def recommend(movie_title, num_recommendations=5):
    #rechercher l'indice du film
    if movie_title not in movies['title'].values:
        return 'Film non trouvé'
    #index du film
    movie_idx = movies[movies['title'] == movie_title].index[0]
    #score de similarité
    similar_movies = similarity_matrix[movie_idx]
    #associer les indices avec leur score de similarité
    similar_movies = list(enumerate(similar_movies))
    #trier par score decroissant et exclure le film lui-même
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]
    #retourner les indices des films recommandés
    recommended_titles = [movies.iloc[i[0]]['title'] for i in similar_movies]


    return recommended_titles[:num_recommendations]

 

    
    
    


