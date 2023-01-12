# import modules
import requests
import json
import pandas as pd
import sqlite3

# Create variables
statYear = '2022'
apiJsonFile = 'nhlPlayers_' + statYear + '.json'
stageJsonFile = 'stageNHLPlayers_' + statYear + '.json'
apiKey = '8e39f5323e0a4e9f8b61e6ff35e16a85'
url = 'https://api.sportsdata.io/v3/nhl/stats/json/PlayerSeasonStats/2022?key=' + apiKey

# API Call Function
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
api_Call()

# Filtered json columns
#df = pd.read_json(apiJsonFile)
#print(df[["StatID","TeamID","PlayerID","SeasonType","Season","Name","Team","Position","GlobalTeamID","Games","Minutes","Seconds","Goals","Assists","ShotsOnGoal","PowerPlayGoals","ShortHandedGoals","EmptyNetGoals","PowerPlayAssists","ShortHandedAssists","HatTricks","ShootoutGoals","PlusMinus","PenaltyMinutes","Blocks","Hits","Takeaways","Giveaways","FaceoffsWon","FaceoffsLost","Shifts","GoaltendingMinutes","GoaltendingSeconds","GoaltendingShotsAgainst","GoaltendingGoalsAgainst","GoaltendingSaves","GoaltendingWins","GoaltendingLosses","GoaltendingShutouts","Started","BenchPenaltyMinutes","GoaltendingOvertimeLosses"]])

# Connect to DB and load Staging
try:
    sqliteConnection = sqlite3.connect('NHL_stats.db')
    cursor = sqliteConnection.cursor()

    df = pd.read_json(apiJsonFile)
    stats = df[["StatID","TeamID","PlayerID","SeasonType","Season","Name","Team","Position","GlobalTeamID","Games","Minutes","Seconds","Goals","Assists","ShotsOnGoal","PowerPlayGoals","ShortHandedGoals","EmptyNetGoals","PowerPlayAssists","ShortHandedAssists","HatTricks","ShootoutGoals","PlusMinus","PenaltyMinutes","Blocks","Hits","Takeaways","Giveaways","FaceoffsWon","FaceoffsLost","Shifts","GoaltendingMinutes","GoaltendingSeconds","GoaltendingShotsAgainst","GoaltendingGoalsAgainst","GoaltendingSaves","GoaltendingWins","GoaltendingLosses","GoaltendingShutouts","Started","BenchPenaltyMinutes","GoaltendingOvertimeLosses"]]

    stats.to_sql('stage_NHL_stats', sqliteConnection, if_exists = 'replace', index = False)
    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
