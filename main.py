import requests

def weather(city_name, api_key):

    url = "http://api.weatherstack.com/current"

    params = {
        "access_key" : api_key,
        "query" : city_name
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if "current" in data:
            temperature = data["current"]["temperature"]
            print(f"The temperature in {city_name} is {temperature}")
        else:
            print("No data for this city.")

    except requests.exceptions.RequestException as e:
        print(f"An error occured {e}")

if __name__ == "__main__":

    api_key ="741dfd459e8352b5c9425e911fb29de1"
    city = input("Enter city: ")
    weather(city, api_key)
