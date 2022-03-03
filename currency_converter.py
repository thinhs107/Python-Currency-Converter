import json as js
import math
import requests


def init_request(response_url):
    try:
        response = requests.get(response_url)
        return response.json()

        response.close()
    except requests.exceptions.HTTPError as err:
        raise print(SystemExit(err))
    return print("True")


def get_country_currency(country_input):
    # Opening JSON file
    f = open('../List_Of_Countries_Currency.json')
    data = js.load(f)
    # print(type(data))

    for item in data.values():
        if item['Country'] == country_input:
            Currency_Code = {item["Currency Code"]}
            return Currency_Code
            break


if __name__ == "__main__":
    #  Country Currency that users wish to convert
    Country_Input = input("Country Currency: ")
    # print(get_country_currency(Country_Input))
    Currency_Code = str((get_country_currency(Country_Input))).strip('{}').replace("'", "")
    # print(Currency_Code)

    # Get UserInput
    User_Input = input("Currency Amount Value: ")
    print(f'{User_Input} Dollar equals')

    API_KEY = "d6a34c30-93b0-11ec-95c1-a71de0b43ca2"
    BASE_URL = "&base_currency=USD"

    MASTER_URL = "https://freecurrencyapi.net/api/v2/latest?apikey=" + API_KEY + BASE_URL

    currency_data = init_request(MASTER_URL)
    current_rate = (currency_data.get("data")[Currency_Code])

    convert_currency = int(User_Input) * current_rate
    print(f'{convert_currency} in {Country_Input}')
