import sqlite3
import pandas as pd

# Charger le CSV
df = pd.read_csv("../Data/clean_dataset.csv")

# Connexion à SQLite
conn = sqlite3.connect("../Data/dataset.db")
cursor = conn.cursor()

# Création de la table
cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY,
    type TEXT,
    domain TEXT,
    contenu TEXT,
    clean_text TEXT
)
""")

# Insertion des données
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO documents (id, type, domain, contenu, clean_text)
    VALUES (?, ?, ?, ?, ?)
    """, (
        int(row["id"]),
        row["type"],
        row["domain"],
        row["contenu"],
        row["clean_text"]
    ))

conn.commit()
conn.close()

print("SQLite database created successfully!")
