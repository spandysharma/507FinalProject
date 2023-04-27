'''Main file for accessing, organization and handling of data.'''
import json
import requests
import flask

clientId = "cjrl47h8vj7xu45bluva17is0fpb0c"
clientSecret = "3b03ng6xwetf5l0zanbzvmkc3wuea2"

access = "https://id.twitch.tv/oauth2/token?client_id=cjrl47h8vj7xu45bluva17is0fpb0c&client_secret=3b03ng6xwetf5l0zanbzvmkc3wuea2&grant_type=client_credentials"
a = requests.post(access)
aData = a.json()

accessToken = aData["access_token"]
print(accessToken)

myobj = \
{"Client-ID": clientId,
"Authorization": "Bearer " + accessToken,
"Body": "fields *; where id = 1942;"}

preferences = dict()
preferences["genre"] = ""
preferences["numPlayers"] = ""
preferences["companies"] = ""

def performSearch(searchTerm):
    if (searchTerm is not ""):
        reqPath = "https://api.igdb.com/v4/games"
        # data = 'fields name,similar_games.name; search "' + searchTerm + '";'
        # print("Searchterm=",searchTerm, "data=",data)
        data = 'fields name,genres.name; search "' + searchTerm + '";'
        # data = 'fields name,genres,rating,involved_companies.company.name; #search "war";' # for searching by name
        # data = 'fields name,rating; sort rating desc;' #for sorting based on ratings

        # reqPath = "https://api.igdb.com/v4/game_modes"
        # data = ''

        b = requests.post(reqPath, data=data, headers=myobj)
        print(b)
        bData = b.json()
        print(bData)
        return bData
        # from igdb.wrapper import IGDBWrapper
        # wrapper = IGDBWrapper("YOUR_CLIENT_ID", "YOUR_APP_ACCESS_TOKEN")

# Genres
# id 31 = Adventure 
# 33 = Arcade
# 10 = Racing
# 9 = Puzzle

genreLog = {"Adventure": 31 , "Arcade": 33 , "Racing": 10, "Puzzle": 9, "Strategy": 15, "Simulator": 13, "Indie": 32}
# genreLog = {31: "Adventure" , 33: "Arcade", 10: "Racing", 9: "Puzzle"}

# def idsToNames(ids):
#     genreNames = []
#     for currId in

def performSearchMCQ(genre):
    filteredResults = []
    # if (preferencesDict["genre"] is not "" and preferencesDict["numPlayers"] is not ""
    #     and preferencesDict["companies"] is not ""):
    wantedGenre = genre
    print("-----------------------------------------------------")
    print(wantedGenre)
    wantedGenreId = genreLog[wantedGenre]
    
    if (wantedGenre is not ""):
        reqPath = "https://api.igdb.com/v4/games"
        firstData = 'fields name,genres; where genres = ' + str(wantedGenreId) + ';'
        b = requests.post(reqPath, data=firstData, headers=myobj)
        bData = b.json()
        print("bData=====================",bData)
        # for result in bData:
        #     # # print(result)
        #     # if ('genres' in result):
        #     #     ids = result['genres'] # will return a list like [8, 31]
        #     #     if (wantedGenreId in ids):
        #             filteredResults.append(result['name'])
    # return filteredResults
    for result in bData:
        filteredResults.append(result['name'])
    return filteredResults

preferences["genre"] = "Adventure"
print("RESULT-----------")
print(performSearchMCQ("Adventure"))
