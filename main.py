from functions.api_functions import get_access_token, get_tempo_like_calendars
from functions.plot_functions import plot_costs
from functions.datas_functions import load_consumption_data
from functions.calculate_daily_costs import calculate_daily_costs
from constants.api_constants import BASE64_AUTH_STR
from tarifs import prixtempo, prixbase

def main():
    # recup du token
    access_token = get_access_token(BASE64_AUTH_STR)
    
  
    start_date = '2020-01-01'
    end_date = '2021-01-20'

    if access_token:
        
        tempo_calendar = get_tempo_like_calendars(access_token, start_date, end_date)

        if tempo_calendar:
            file_path = 'datas/ma-conso-quotidienne-164-64.csv'
            consumption_data = load_consumption_data(file_path)
            consumption_data = consumption_data[(consumption_data['Date de consommation'] >= start_date) & 
                                                (consumption_data['Date de consommation'] <= end_date)]
            base_rate = next((item['PrixKW'] for item in prixbase if item['Puissance'] == 6), None)

            tempo_rates = prixtempo[0] 

            base_costs, tempo_costs = calculate_daily_costs(consumption_data, tempo_calendar, base_rate, tempo_rates)

            plot_costs(consumption_data['Date de consommation'], base_costs, tempo_costs)
           
            
if __name__ == "__main__":
    main()
