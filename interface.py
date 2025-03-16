import streamlit as st  
from systeme_recommandation import recommend, movies  

st.title('Système de recommandation de films')
st.write('entrez le nom de votre film préféré')
movie_title = st.text_input('titre du film : ')
if st.button('rechercher'):
    if movie_title:
       recommandations = recommend(movie_title)
       st.write('Films recommandés :')
       for rec in recommandations:
           st.write('-',rec)
    else:
       st.write('Veuillez entrer un titre de film')

