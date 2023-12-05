from sklearn.decomposition import KernelPCA
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pickle

from scipy.spatial.distance import cdist

def inference_(responses : np.array):

  model = pickle.load()   # conditionnement choix de modèle question facultatif   // 
  pred = model.predict(responses) 
  return pred

def preprocessing_cluster(df):
    

    var_profil = ['Sexe', 'Age', 'TYPOLOGIE', 'Age tranches', 'CSP', 'Habitat',
           'Taille AA', 'Nb voitures du foyer',
           'Nb voitures hybrides ou électriques', 'Revenus mensuels du foyer',
           'CP', 'Insee', 'AA', 'Foyer', 'Enfants au foyer', 'Nb enfants foyer']

    var_drop  = ['Sensibilité prix','Sensibilté au temps','Sensibilité ecolo','Sensibilité santé' , "Score prix","Sensible au temps" , 'Sensibilité ecolo.1', 'Sensibilité prix.1', 'Sensibilité santé.1']
    var_drop1  = [ i+".1" for i in var_drop]
    var_drop1 = []
    train = df[df.columns.difference(var_profil+var_drop + var_drop1)]

    #df = df.drop("ID" ,axis = 1 )

    train____ = pd.concat([pd.get_dummies(df[[ 'Sexe', 'Age', 'Age tranches', 'CSP', 'Habitat',
           'Nb voitures du foyer',
           'Nb voitures hybrides ou électriques', 'Revenus mensuels du foyer',
       'Foyer', 'Enfants au foyer', 'Nb enfants foyer']]).iloc[:,2:],train],axis = 1)

    return train____



def attribute_cluster(df , label):

    df["label"] = label

  # Nouvelle ligne sans label
   # Exemple de nouvelles caractéristiques

  # Ajouter la nouvelle ligne au DataFrame pour la comparaison


    df_with_new_row = df.copy()
      # Séparer les caractéristiques et les labels
    features = df_with_new_row.drop('label', axis=1, errors='ignore')
    features = features.iloc[: , :-1]
  # Calculer la similarité cosinus
    similarity_matrix =cosine_similarity(features)

  # Similarités de la nouvelle ligne avec toutes les autres
    similarities = similarity_matrix[-1][:-1]  # Exclure la similarité avec elle-même

  # Obtenir les indices des 10 lignes les plus similaires
    top_10_similar_indices = np.argsort(-similarities)[:10]

  # Fréquence des labels parmi les 10 lignes les plus similaires
    top_10_labels = label.iloc[top_10_similar_indices]
    top_10_freq = top_10_labels.value_counts() / len(top_10_labels)

      # Fréquence des labels dans l'ensemble des données
    overall_freq = label.value_counts() / len(label)

      # Calculer le ratio
    penalized_freq = top_10_freq / overall_freq 
    penalized_freq = penalized_freq.sort_values(ascending = False).index[0]
    
    return penalized_freq
  
