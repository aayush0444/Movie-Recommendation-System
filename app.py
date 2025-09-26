import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title_x'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title_x)  # ✅ fixed
    return recommended


# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set page config (title + emoji in browser tab)
st.set_page_config(page_title="Cine Suggest 🎬", page_icon="🍿", layout="centered")

# Title section
st.title("🍿 Cine Suggest 🎬")
st.subheader("Your Personalized Movie Recommendation System")

st.markdown("---")  # horizontal divider

# Highlighted info box
st.success("✨ Welcome to Cine Suggest! Discover your next favorite movie effortlessly.")

# Select movie
selected_movie_name = st.selectbox('🎥 Choose a movie you like:', movies['title_x'])

# Recommend button
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.markdown("### 🔥 Top Recommendations for you:")
    for i in recommendations:
        st.write( i)

# Footer
st.markdown("---")
st.caption("Made by Akr")
