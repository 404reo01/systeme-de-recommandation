# 🎬 Système de Recommandation de Films

Ce projet est un système de recommandation de films utilisant des techniques de traitement du langage naturel (TF-IDF et similarité cosine). Il fournit une liste de films similaires en fonction d'un film donné, avec une interface web interactive créée avec Streamlit.

---

## 🚀 Fonctionnalités

- Recommander des films similaires en fonction de leurs descriptions (`overview`) dans un dataset.
- Interface web interactive permettant aux utilisateurs de saisir un titre de film et d'obtenir des recommandations instantanées.
- Utilise des algorithmes de traitement de texte basés sur **TF-IDF** et **similarité cosinus**.

---

## 📂 Structure du Projet

Le projet est organisé en deux fichiers principaux :

1. **`systeme_recommandation.py`**
   - Contient toute la logique du système de recommandation.
   - Chargement et prétraitement des données (`movies.csv`).
   - Calcul des similarités entre les films.
   - Fonction `recommend_simple()` pour retourner les films recommandés.

2. **`interface.py`**
   - Interface utilisateur construite avec **Streamlit**.
   - Permet à l'utilisateur d'interagir avec le système en saisissant un titre de film.
   - Affiche les recommandations directement dans un navigateur.

---

## 🛠️ Installation

1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/404reo01/systeme-de-recommandation.git
   cd votre-depot
    2. Installez les dépendances nécessaires :
       bash
       pip install pandas scikit-learn streamlit
    3. Placez le fichier movies.csv (dataset des films) dans le même répertoire que le projet. Ce fichier doit inclure les colonnes suivantes :
        ◦ title : Titre du film
        ◦ overview : Description ou synopsis du film
## 🖥️ Utilisation
    1. Assurez-vous que les deux fichiers, systeme_recommandation.py et interface.py, sont dans le même dossier.
    2. Lancez l'application Streamlit à l'aide de la commande suivante :
       bash
       streamlit run interface.py
    3. L'application s'ouvrira automatiquement dans votre navigateur. Entrez le titre d'un film et cliquez sur "Rechercher" pour voir les recommandations.
📊 Technologies Utilisées
    • Python : Langage principal pour le développement.
    • Pandas : Manipulation des données.
    • Scikit-learn : Calcul TF-IDF et similarité cosine.
    • Streamlit : Création de l'interface utilisateur.
✨ Prochaines Améliorations
    • Ajouter des filtres basés sur les genres ou la popularité des films.
    • Inclure des images ou des affiches de films dans l'interface.
    • Étendre la base de données pour inclure davantage de films.
📜 Licence
Ce projet est sous licence libre MIT.

