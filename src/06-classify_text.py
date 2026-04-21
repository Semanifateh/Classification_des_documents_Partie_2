import joblib
import numpy as np
import tensorflow as tf

# 1. Chargement des outils sauvegardés
tfidf = joblib.load("../models/tfidf_vectorizer.pkl")
model = tf.keras.models.load_model("../models/medical_model_final.h5")
le = joblib.load("../models/label_encoder.pkl")

def predire_categorie(texte_brut):
    texte_nettoye = texte_brut.lower()    
    vecteur_sparse = tfidf.transform([texte_nettoye])
    vecteur_dense = vecteur_sparse.toarray().astype('float32')
    prediction = model.predict(vecteur_dense, verbose=0)
    classe_index = np.argmax(prediction)
    classe_nom = le.inverse_transform([classe_index])[0]
    probabilite = prediction[0][classe_index] * 100
    
    return classe_nom, probabilite

# ==========================================
# 2. Test
# ==========================================

with open("../Data/Document7.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

# remplacer les retours à la ligne par des espaces
contenu = contenu.replace("\n", " ")

print("--- Résultat ---")

categorie, confiance = predire_categorie(contenu)

print(f"\nTexte : {contenu[:200]}...")
print(f"Résultat : {categorie} ({confiance:.2f}% de confiance)")
