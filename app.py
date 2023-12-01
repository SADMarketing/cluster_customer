import pandas as pd 
import streamlit as st

# Fonction pour créer une question avec des boutons radio
def creer_question(titre, options, cle):
    st.subheader(titre)
    return st.radio("", options, key=cle)

with open(link_file_question) as file  : 
    
# Liste des questions
questions = ["Je privilégie les soldes/ventes privées pour acheter des produits non alimentaires et ainsi faire de bonnes affaires",
"J’achète des produits de seconde main (vêtements, meubles, jouets...) pour que cela me coûte moins cher",
"J’utilise les facilités de paiement (3, 4, 10 fois) quand cela est possible" , 
"Je fais très attention à mon budget pour les courses alimentaires" , 
"Je fais très attention à mon budget pour des achats non alimentaires (vêtements, meubles, jouets...)" ,
"J’achète très souvent le produit le moins cher",
"Je cherche les promotions quand je fais des achats alimentaires",
"Je peux souscrire à un crédit à la consommation pour un produit que je veux vraiment" , 
"J’ai du mal à boucler mes fins de mois" , 
"J’arrive à m’octroyer un budget restaurant / loisirs",
"Je suis capable de dépenser une grosse somme d’argent (> 500€) pour un produit qui me fait plaisir" , 
"J’arrive à épargner tous les mois ou presque",        # last question argent 
             "J’aime passer du temps sur internet à chercher le produit que je veux m’acheter" , 
"Je fais des recherches internet pour gagner du temps en magasin" , 
"Je préfère le drive ou la livraison vs l’hypermarché / supermarché, c’est plus rapide" , 
"Je me fais livrer régulièrement de la restauration (hamburgers, sushis, pizzas...)" , 
"J’accorde beaucoup d’importance au délai de livraison, il faut que ma commande arrive très rapidement" , 
"Je préfère acheter en ligne plutôt qu’en magasin, c’est plus rapide" , 
"Je peux faire plus de 20 minutes de route pour me rendre dans un magasin ou centre commercial que j’aime" , 
"Je choisis le magasin le plus proche pour ne pas perdre de temps" , 
"J’aime passer du temps à faire du shopping en magasin" , 
            "Je consomme des produits surgelés ou préparés pour gagner du temps"  , 
"J’ai l’impression de courir après le temps" , 
"Je suis bien organisé / je gère mon temps efficacement" , # last question temps 
             
"Je prends volontiers l’avion pour partir en vacances" , 
"J’achète des produits de seconde main (vêtements, meubles, jouets...), pour réduire mon empreinte écologique" , 
"Je trie mes déchets chez moi (carton/ plastique, déchets verts, verre, tout venant)",
"J’aime acheter de nouveaux produits régulièrement, j’adore faire du shopping", 
"Je consomme local (produits Français voire régionaux) et de saison" , 
"Je me déplace à pied, à vélo ou en transports en commun (je ne prends pas la voiture) quand cela est possible" , 
"Je limite les emballages et le plastique / Je refuse les sachets ou emballages / Je viens avec mes propres contenants ou sacs superflus quand cela est possible" , 
"Je revends ou donne (vêtements, meubles, jouets...) plutôt que jeter" , 
"J'évite les enseignes de fast-fashion (Primark, H&M, Zara...) pour éviter de surconsommer" , 
"Je préfère acheter bio, je pense que c’est meilleur pour la Terre" , 
"L’écologie est un critère important dans mes actes d’achat" , # last question ecologie 
             "Je préfère consommer moins mais des produits de meilleure qualité" , 
"Je préfère acheter bio, je pense que c’est meilleur pour ma santé" , 
"La composition des produits (liste des ingrédients) que j’achète est importante pour moi",
"Je consomme des compléments alimentaires plusieurs fois dans l’année" , 
"Je fais du sport au moins une fois par semaine",
"Je consomme régulièrement des fast-foods" , 
"Je limite les produits avec du gluten et/ou avec du lactose" , 
"Je suis sensible aux allégations nutritionnelles sur les packagings (nutriscore, labels...)" , 
"Je préfère acheter des produits bruts (ex : légumes, pâtes, farine...) que des produits transformés, industriels (ex : plats préparés, pizzas, biscuits...)" , 
"Je fume tous les jours et/ou je bois de l’alcool plusieurs fois par semaine" , 
"J’ai une alimentation équilibrée" , 
"Je fais très attention à ma santé" # last question santé




]

# Créer les questions et stocker les réponses
reponses = {}
for i, question in enumerate(questions, start=1):
    reponses[question] = creer_question(f"{i}. {question}", 
                                        ["Tout à fait d'accord", "Plutôt d'accord", "Plutôt pas d'accord", "Pas du tout d'accord"],
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
