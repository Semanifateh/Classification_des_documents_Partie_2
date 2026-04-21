# 🧠 Classification de Documents Médicaux
### Pipeline NLP & Deep Learning

## 📌 Description

Ce projet propose un pipeline complet de Traitement Automatique du Langage Naturel (NLP) permettant de classifier automatiquement des documents textuels en deux catégories :

- Médical
- Non Médical

Le système couvre :
- Prétraitement du texte
- Gestion des données
- Vectorisation
- Entraînement d’un modèle de Deep Learning
- Prédiction sur nouveaux documents

---

## 🚀 Structure du projet

.
├── Data
│   ├── clean_dataset.csv
│   ├── data.csv
│   ├── dataset.db
│   └── Documents*
│
├── Documents
│   └── Documents.pdf
│
├── models
│   ├── label_encoder.pkl
│   ├── medical_model_final.h5
│   └── tfidf_vectorizer.pkl
│
├── src
│   ├── 01-nltk.ipynb
│   ├── 02-creation_data_sql.py
│   ├── 03-vectorisation.ipynb
│   ├── 04-entrainement.ipynb
│   ├── 05-extract_pdf.py
│   └── 06-classify_text.py
│
└──README.md

---

## 📁 Dossiers importants

### models/
- tfidf_vectorizer.pkl : vectoriseur TF-IDF
- label_encoder.pkl : encodeur des labels
- medical_model_final.h5 : modèle MLP entraîné

### Documents/
- Fichiers PDF à tester
- Extraction via 05-extract_pdf.py

### Data/
- clean_dataset.csv : dataset nettoyé
- dataset.db : base SQLite générée
- Document.txt : fichier utilisé pour les tests  
---

## ⚙️ Pipeline

### 1. Prétraitement (01-nltk.ipynb)
- Tokenisation
- Stopwords
- Lemmatisation
- Normalisation

### 2. Base de données (02-creation_data_sql.py)
- Création dataset.db


### 3. Vectorisation (03-vectorisation.ipynb)
- TF-IDF
- 5000 features

### 4. Modèle (04-entrainement.ipynb)
- MLP (Dense + Dropout)
- Adam optimizer
- 20 epochs

### 5. PDF extraction
- PyMuPDF

### 6. Classification
- Prédiction + probabilité

---

## 📊 Résultats

- Très bonne précision (~99–100%)
- Bonne classification médicale/non médicale

Limite :
- Sous-domaines médicaux insuffisants

---

## 💻 Installation

pip install nltk pandas scikit-learn tensorflow sqlalchemy pymupdf joblib

---

## ▶️ Exécution

1. 01-nltk.ipynb
2. 02-creation_data_sql.py
3. 03-vectorisation.ipynb
4. 04-entrainement.ipynb
5. python src/05-extract_pdf.py
6. python src/06-classify_text.py

---

## 🔮 Améliorations

- Classification multi-classes
- Word2Vec / BERT
- Application .exe
- Interface web
