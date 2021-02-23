import requests
from twilio.rest import Client

#######  API #########################################

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = 'ACfcccfa237533da962ebfb52d506127de'
auth_token = '91f5194e4f48410c5145248f64f00cf6'

parameters = {
    "lat": 34.693737,
    "lon": 135.502167,
    "appid": "f34f8020b4bea937b914cd4618cf98ef",
    "exclude": "current,minutely,daily",
    "lang": "ja",
    "units": "metric"


}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status
data = response.json()
morning_data_1 = data["hourly"][0]["weather"][0]["description"]
morning_data_2 = data["hourly"][1]["weather"][0]["description"]
daytime_data_1 = data["hourly"][6]["weather"][0]["description"]
daytime_data_2 = data["hourly"][7]["weather"][0]["description"]
evening_data_1 = data["hourly"][12]["weather"][0]["description"]
evening_data_2 = data["hourly"][13]["weather"][0]["description"]

################  Twillio ############################################

client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body=f"朝の散歩の行きは{morning_data_1}帰りは{morning_data_2}\nお昼の散歩の行きは{daytime_data_1}帰りは{daytime_data_2}\n夜の散歩の行きは{evening_data_1}帰りは{evening_data_2}",
                     from_='+17867417376',
                     to='+819066744761'
                 )

print(message.status)





