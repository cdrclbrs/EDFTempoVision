import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def plot_tempo_colors(data):

    if 'tempo_like_calendars' in data and 'values' in data['tempo_like_calendars']:
        values_list = data['tempo_like_calendars']['values']

        dates = []
        colors = []

        for item in values_list:
            start_date_str = item['start_date']
            color = item['value']
            date = datetime.strptime(start_date_str, '%Y-%m-%dT%H:%M:%S%z').date()

            dates.append(date)
            colors.append(color)

       
        color_map = {'BLUE': 1, 'WHITE': 2, 'RED': 3}
        numerical_values = [color_map[val] for val in colors]

        plt.figure(figsize=(10, 6))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.plot(dates, numerical_values, marker='o', linestyle='-')
        plt.yticks([1, 2, 3], ['BLUE', 'WHITE', 'RED'])
        plt.xlabel('Date')
        plt.ylabel('Couleur Tempo')
        plt.title('Couleurs Tempo')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def plot_costs(dates, base_costs, tempo_costs):

    plt.figure(figsize=(12, 6))
    plt.plot(dates, base_costs, label='Tarif Base', color='blue')
    plt.plot(dates, tempo_costs, label='Tarif Tempo', color='red')
    plt.xlabel('Date')
    plt.ylabel('Coût (€)')
    plt.title('Coûts Quotidiens d\'Électricité')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
