import requests

url = "https://meteostat.p.rapidapi.com/point/monthly"

querystring = {"lat":"52.5244","lon":"13.4105","alt":"43","start":"2020-01-01","end":"2020-12-31"}

headers = {
	"x-rapidapi-key": "e74f6e6e70msh5ffc80a87df5e8cp1e58b3jsn794d075afa9c",
	"x-rapidapi-host": "meteostat.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())