import pandas as pd

def load_consumption_data(file_path):

    df = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';', skiprows=1)

    # Convertir la colonne des dates en format datetime
    # Assurez-vous que le nom de la colonne de date dans votre fichier CSV est correctement spécifié ici
    df['Date de consommation'] = pd.to_datetime(df['Date de consommation'], format='%d/%m/%Y')

    return df
