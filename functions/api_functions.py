import requests
import base64

def get_access_token(base64_auth_str):
    """
    recupere un access token pour l' auth  API 

    :param base64_auth_str: Base64 encoded client ID + secret.
    :return: Access token string or None in case of failure.
    """
    token_url = "https://digital.iservices.rte-france.com/token/oauth"
    headers = {
        "Authorization": f"Basic {base64_auth_str}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Error obtaining token:", response.status_code)
        print(response.text)
        return None

def get_tempo_like_calendars(access_token, start_date, end_date):
    """
    Sert a toper les donnees de l API.

    :param access_token: Access token .
    :param start_date: au format 'YYYY-MM-DD' .
    :param end_date: au format 'YYYY-MM-DD' .
    :return: Data from the API or None in case of failure.
    """
    api_url = "https://digital.iservices.rte-france.com/open_api/tempo_like_supply_contract/v1/tempo_like_calendars"

    # Add time and timezone offset to the dates
    start_date_str = f"{start_date}T00:00:00+02:00"
    end_date_str = f"{end_date}T00:00:00+02:00"

    params = {
        'start_date': start_date_str,
        'end_date': end_date_str,
        'fallback_status': 'true'
    }

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json'
    }

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        print(response.text)
        return None
