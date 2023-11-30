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
  
