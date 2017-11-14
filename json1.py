import json 
from urllib.request import urlopen

def getCountry(ipAddress):
	response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
	responseJson = json.loads(response)
	return responseJson.get("country_code")
def getCountryName(ipAddress):
	response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
	responseJson = json.loads(response)
	return responseJson.get("country_name")
print(getCountry("111.21.39.46"),getCountryName("111.21.39.46"))