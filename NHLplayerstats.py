# import modules
import requests
import json
import pandas as pd

# Create variables
statYear = '2022'
apiJsonFile = 'nhlPlayers_' + statYear + '.json'
stageJsonFile = 'stageNHLPlayers_' + statYear + '.json'
apiKey = '8e39f5323e0a4e9f8b61e6ff35e16a85'
url = 'https://api.sportsdata.io/v3/nhl/stats/json/PlayerSeasonStats/2022?key=' + apiKey


def api_Call():
    # Call API with key
    response = requests.get(url)

    #print(response)

    # Response results as json
    player = response.json()

    # Saves response results as a json file
    jsonString = json.dumps(player)
    jsonFile = open(apiJsonFile,"w")
    jsonFile.write(jsonString)
    jsonFile.close()

# API Call Function


# Filtered json columns


# Connect to DB and load Staging
