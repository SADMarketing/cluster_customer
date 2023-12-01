import pandas as pd 
import streamlit as st

# Fonction pour créer une question avec des boutons radio
def creer_question(titre, options, cle):
    st.subheader(titre)
    return st.radio("", options, key=cle)

#with open(link_file_question) as file  : 

# Sexe
sexe = st.radio(
    "Etes-vous ?",
    ('Un homme', 'Une femme', 'Autre')
)

# Âge
age = st.text_input("Quel est votre âge ?")

# Profession
profession = st.selectbox(
    "Quelle est votre profession ?",
    ('Agriculteur exploitant', 'Artisan, commerçant, chef d’entreprise', 'Cadre, profession libérale',
     'Profession intermédiaire', 'Employé', 'Ouvrier', 'Retraité', 'Sans activité', 'Etudiant')
)

# Habitation
habitation = st.radio(
    "Habitez-vous ?",
    ('En maison', 'En appartement')
)

# Code Postal
code_postal = st.text_input("Quel est votre code postal ?")
# Ici vous devez ajouter la logique pour recoder en rural / urbain / péri-urbain

# Nombre de personnes dans le foyer
nombre_personnes = st.selectbox(
    "Combien de personnes vivent dans votre foyer ?",
    ['1 personne (je vis seul.e)', '2 personnes', '3 personnes', '4 personnes', '5 personnes et +']
)

# Enfants dans le foyer
enfants = st.radio(
    "Avez-vous des enfants qui vivent avec vous ?",
    ('Oui', 'Non')
)

# Si oui, combien d'enfants
if enfants == 'Oui':
    nb_enfants = st.number_input("Si oui, combien ?", min_value=1, max_value=10)

    # Âges des enfants
    ages_enfants = {}
    for i in range(1, nb_enfants + 1):
        ages_enfants[f'Enfant {i}'] = st.text_input(f"Quel âge a l'enfant {i} ?")

# Voitures dans le foyer
voitures = st.selectbox(
    "Combien de voitures possédez-vous au sein du foyer ?",
    ('Aucune', '1 voiture', '2 voitures', '3 voitures ou +')
)

# Voitures hybrides ou électriques
voitures_hybrides_electriques = st.selectbox(
    "Parmi les voitures de votre foyer, quel est le nombre de voitures hybrides ou électriques ?",
    ('Aucune voiture hybride ou électrique', '1 voiture hybride ou électrique', '2 voitures hybrides ou électriques', '3 voitures hybrides ou électriques ou +')
)

# Revenus mensuels
revenus = st.selectbox(
    "Quels sont les revenus mensuels de votre foyer (nets, allocations comprises) ?",
    ('Moins de 750€', '750-1150€', '1150-1500€', '1500-2300€', '2300-3000€', '3000-4500€', '4500-6100€', '6100-7600€', 'Plus de 7600€', 'Préfère ne pas répondre / ne sait pas')
)

    
# Liste des questions
questions = [  'Je fais très attention à mon budget pour les courses alimentaires',
       'Je fais très attention à mon budget pour des achats non alimentaires (vêtements, meubles, jouets...)',
       'J’achète très souvent le produit le moins cher',
       'J’ai du mal à boucler mes fins de mois',
       'J’arrive à épargner tous les mois ou presque', 
       'J’aime passer du temps sur internet à chercher le produit que je veux m’acheter',
       'Je fais des recherches internet pour gagner du temps en magasin',
       'Je préfère le drive ou la livraison vs l’hypermarché supermarché, c’est plus rapide',
       'Je me fais livrer régulièrement de la restauration (hamburgers, sushis, pizzas...)',
       'J’accorde beaucoup d’importance au délai de livraison, il faut que ma commande arrive très rapidement',
       'Je préfère acheter en ligne plutôt qu’en magasin, c’est plus rapide',
       'Je choisis le magasin le plus proche pour ne pas perdre de temps',
       'Je consomme des produits surgelés ou préparés pour gagner du temps',
       'Je prends volontiers l’avion pour partir en vacances',
       'J’achète des produits de seconde main (vêtements, meubles, jouets...), pour réduire mon empreinte écologique',
       'Je me déplace à pied, à vélo ou en transports en commun (je ne prends pas la voiture) quand cela est possible',
       'Je limite les emballages et le plastique Je refuse les sachets ou emballages Je viens avec mes propres contenants ou sacs superflus quand cela est possible',
       "J'évite les enseignes de fast-fashion (Primark, H&M, Zara...) pour éviter de surconsommer",
       'Je préfère acheter bio, je pense que c’est meilleur pour la Terre',
       'L’écologie est un critère important dans mes actes d’achat',
       'Je préfère consommer moins mais des produits de meilleure qualité',
       'Je préfère acheter bio, je pense que c’est meilleur pour ma santé',
       'Je fais du sport au moins une fois par semaine',
       'Je consomme régulièrement des fast-foods',
       'Je fume tous les jours et ou je bois de l’alcool plusieurs fois par semaine',
       'J’ai une alimentation équilibrée', 'Je fais très attention à ma santé'  




]

# Créer les questions et stocker les réponses
reponses = {}
for i, question in enumerate(questions, start=1):
    reponses[question] = creer_question(f"{i}. {question}", 
                                        ["Tout à fait d'accord", "Plutôt d'accord", "Plutôt pas d'accord", "Pas du tout d'accord"],
                                        cle=f"question_{i}")
import streamlit as st

# Page header
st.header("Enquête sur les habitudes d'achat et informations personnelles")


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
