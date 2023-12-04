from datetime import datetime

def calculate_tempo_cost(consumption, day_type, tempo_rates):
    """
    Calcule le coût pour un jour en fonction du tarif Tempo.

    :param consumption: Consommation quotidienne en kWh.
    :param day_type: Type du jour ('BLUE', 'WHITE' ou 'RED').
    :param tempo_rates: Dictionnaire des tarifs pour le tarif Tempo.
    :return: Coût pour le jour.
    """
    rate_key = f'{day_type}_HP'  # En supposant que le tarif HP est à utiliser, à ajuster si nécessaire
    rate = tempo_rates.get(rate_key, 0)
    return (consumption * rate)/100

def calculate_base_cost(consumption, base_rate):
    """
    Calcule le coût pour un jour en fonction du tarif de Base.

    :param consumption: Consommation quotidienne en kWh.
    :param base_rate: Tarif pour le tarif de Base.
    :return: Coût pour le jour.
    """
    return (consumption * base_rate)/100

def calculate_daily_costs(consumption_data, tempo_calendar, base_rate, tempo_rates):
    """
    Calcule les coûts quotidiens en utilisant les tarifs Base et Tempo.

    :param consumption_data: DataFrame avec les données de consommation quotidienne.
    :param tempo_calendar: Dictionnaire indiquant le type de chaque jour pour le tarif Tempo.
    :param base_rate: Tarif pour le tarif de Base.
    :param tempo_rates: Dictionnaire des tarifs pour le tarif Tempo.
    :return: Deux listes contenant les coûts quotidiens pour les tarifs Base et Tempo.
    """
    base_costs = []
    tempo_costs = []

    # Assurez-vous que les dates dans tempo_calendar sont au bon format
    tempo_days = tempo_calendar['tempo_like_calendars']['values']
    formatted_tempo_calendar = {datetime.strptime(day['start_date'], '%Y-%m-%dT%H:%M:%S%z').date(): day['value'] 
                                for day in tempo_days}

    for index, row in consumption_data.iterrows():
        # Extraire la date et la consommation
        date = row['Date de consommation'].date()
        consumption = row['Consommation (kWh)']

        # coût pour le tarif de Base
        base_cost = (consumption * base_rate)/100
        base_costs.append(base_cost)

        # type de jour et le tarif Tempo associé
        day_type = formatted_tempo_calendar.get(date, 'BLUE')
        tempo_rate = tempo_rates.get(f'{day_type}_HP', base_rate)  # tarif Base si aucun tarif Tempo n'est trouvé

        # coût pour le tarif Tempo
        tempo_cost = (consumption * tempo_rate)/100
        tempo_costs.append(tempo_cost)

    return base_costs, tempo_costs
