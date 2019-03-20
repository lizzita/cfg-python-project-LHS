import requests as re

pd = {'q':'Sheffield, UK', 'units':'metric', 'appid':"84600bca7507293656495e8972aec659"}

endpoint = "http://api.openweathermap.org/data/2.5/weather"

def query_weather(payload1, endpoint):
    # endpoint = "http://api.openweathermap.org/data/2.5/weather"
    response = re.get(endpoint, params=payload1)

    return response

response1 = query_weather(pd, endpoint)

if response1.status_code == 200:
    print(response1.text)
else:
    response1 = query_weather(pd, endpoint)

def jsonify(response):
    json_response = response1.json()
    return json_response

json_response = jsonify(response1)
print("\n")
print(json_response)

print(json_response['main']['temp'])

temp = json_response['main']['temp']

#if temp < 10:
 #   start_boiler()
#else:
 #   leave_it_off()