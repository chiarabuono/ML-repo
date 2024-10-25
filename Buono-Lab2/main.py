import pandas as pd

# Carica il file CSV
df = pd.read_csv("turkish-se-SP500vsMSCI.csv")

# Stampa l'intero DataFrame per vedere i dati caricati
print(df)
print("...................")

# Controlla il nome delle colonne
print(df.columns)  # Stampa i nomi delle colonne per vedere come sono chiamate

# Estrai due colonne specifiche utilizzando i nomi delle colonne
colonna1 = df["-0.004679315"].tolist()  # Sostituisci 'NomeColonna1' con il nome reale
colonna2 = df["0.012698039"].tolist()  # Sostituisci 'NomeColonna2' con il nome reale

# Stampa le due liste
for line in colonna1:
    print(line)
