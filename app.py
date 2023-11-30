import pandas as pd 
import streamlit as st

# Fonction pour créer une question avec des boutons radio
def creer_question(titre, options, cle):
    st.subheader(titre)
    return st.radio("", options, key=cle)

# Liste des questions
questions = [
    "Autoriser l'adoption pour les couples homosexuels",  # Ajoutez plus de questions ici
]

# Créer les questions et stocker les réponses
reponses = {}
for i, question in enumerate(questions, start=1):
    reponses[question] = creer_question(f"{i}. {question}", 
                                        ["Très favorable", "Plutôt favorable", "Plutôt défavorable", "Très défavorable"],
                                        cle=f"question_{i}")

# Boutons de navigation
col1, col2 = st.columns(2)
with col1:
    if st.button("Précédent"):
        # Implémentez la logique pour revenir à la question précédente
        pass

with col2:
    if st.button("Suivant"):
        # Implémentez la logique pour passer à la question suivante
        pass

# Bouton de prédiction (à placer à la dernière page)
if st.button("Prédiction"):
    np.array(reponses) 
    
    # Implémentez ici la logique de prédiction en utilisant les réponses collectées
    st.write("Résultat de la prédiction")
