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

def inference(responses : np.array):

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
  
