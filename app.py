import os
import streamlit as st
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define absolute path for movies.csv
CSV_PATH = os.path.join(os.getcwd(), 'movies.csv')


@st.cache_data
def load_data():
    df = pd.read_csv('movies.csv')
    df['overview'] = df['overview'].fillna('')
    return df

movies_data = load_data()

# TF-IDF setup
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies_data['overview'])
similarity = cosine_similarity(tfidf_matrix)

# Recommender function
def recommend_movie(movie_name, n=5):
    movie_names = movies_data['title'].tolist()
    close_matches = difflib.get_close_matches(movie_name, movie_names)
    if not close_matches:
        return []
    closest_match = close_matches[0]
    index = movies_data[movies_data.title == closest_match].index[0]
    similarity_scores = list(enumerate(similarity[index]))
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    recommendations = [movies_data.iloc[i[0]]['title'] for i in sorted_movies]
    return recommendations

# Streamlit UI
st.title("🎬 Movie Recommender")
st.write("Type a movie you like, and get similar recommendations!")

movie_input = st.text_input("Enter movie name:")

if movie_input:
    with st.spinner('Finding recommendations...'):
        results = recommend_movie(movie_input)
        if results:
            st.success(f"Top recommendations for '{movie_input}':")
            for movie in results:
                st.write(f"- {movie}")
        else:
            st.error("Movie not found. Try a different title.")
