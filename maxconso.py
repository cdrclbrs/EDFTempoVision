import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def load_data(file_path):
    df = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1')
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['heure'])
    df['Date'] = df['DateTime'].dt.date
    df['Hour'] = df['DateTime'].dt.hour
    return df

# calcul conso par heure
def calculate_hourly_consumption(df):
    df.sort_values(by='DateTime', inplace=True)
    df['Consommation'] = df['puissance'].diff().fillna(0).clip(lower=0)
    hourly_data = df.groupby(['Date', 'Hour'])['Consommation'].sum().reset_index()
    return hourly_data


def find_peak_consumption(hourly_data):
    peak_consumption = hourly_data.loc[hourly_data.groupby('Date')['Consommation'].idxmax()]
    peak_consumption['Month'] = peak_consumption['Date'].apply(lambda x: x.month)
    return peak_consumption


def plot_peak_consumption(peak_consumption):
    plt.figure(figsize=(12, 6))
    for _, row in peak_consumption.iterrows():
        month = row['Month']
        hour = row['Hour']
        plt.scatter(hour, month, c='red', s=10)

    plt.xlabel('Heure de la journée')
    plt.ylabel('Mois de l\'année')
    plt.title('Heure de consommation maximale par jour sur une année')
    plt.xticks(range(24))
    plt.yticks(range(1, 13))
    plt.grid(True)
    plt.tight_layout()
    plt.show()


file_path = 'datas/mes-puissances-atteintes-30min-cleaned.csv'
df = load_data(file_path)
hourly_consumption = calculate_hourly_consumption(df)
peak_consumption = find_peak_consumption(hourly_consumption)
plot_peak_consumption(peak_consumption)
