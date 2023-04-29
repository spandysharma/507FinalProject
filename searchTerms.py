'''Main file for accessing, organization and handling of data.'''
import json
import requests
import flask

################################################################################

'''Double authetication process for logging and using IGDB API'''

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
"Body": "fields *;"}

def performSearch(searchTerm):
    '''performs user search based on text input'''

    if (searchTerm is not ""):
        reqPath = "https://api.igdb.com/v4/games"
        data = 'fields name,genres.name; search "' + searchTerm + '";'

        b = requests.post(reqPath, data=data, headers=myobj)
        print(b)
        bData = b.json()
        print(bData)
        return bData

################################################################################

'''Offering limited options for categories'''

genreLog = {"Adventure": 31 , "Arcade": 33 , "Racing": 10, "Puzzle": 9, "Strategy": 15, "Simulator": 13, "Indie": 32}

franchiseLog = {"Pac-Man": 892, "Austin Powers": 783, 'My Guardian Characters': 3798, "The Simpsons": 2214, "Bladerite": 4543, "Medabots": 450,
                "Aeon Flux": 751, "Gradius": 775, 'Devil May Cry': 834, "Castle": 936}

platformLog = {'Commodore CDTV': 158, 'Sega Pico': 339, 'PlayStation 2': 8, 'iOS': 39, 'Commodore Plus/4': 94, 
               'AY-3-8710': 144, 'Odyssey': 88, 'Commodore PET': 90, 'Sol-20': 237, 'PC (Microsoft Windows)': 6}

ratingLog = [8,9,10,13,20]

################################################################################

def searchByCategory(category):
    '''takes different 4 categories (genre, platform, franchise, age rating)
    and gives further input options to the user'''

    if (category in genreLog):
        filteredResults = []
        wantedGenre = category
        wantedGenreId = genreLog[wantedGenre]
        
        if (wantedGenre is not ""):
            reqPath = "https://api.igdb.com/v4/games"
            firstData = 'fields name,genres; where genres = ' + str(wantedGenreId) + ';'
            b = requests.post(reqPath, data=firstData, headers=myobj)
            bData = b.json()

        for result in bData:
            filteredResults.append(result['name'])
        return filteredResults


    elif (category in franchiseLog):
        filteredResults = []
        wantedFranchise = category
        wantedFranchiseId = franchiseLog[wantedFranchise]
        
        if (wantedFranchise is not ""):
            reqPath = "https://api.igdb.com/v4/games"
            firstData = 'fields name,franchises; where franchises = ' + str(wantedFranchiseId) + ';'
            b = requests.post(reqPath, data=firstData, headers=myobj)
            bData = b.json()

        for result in bData:
            filteredResults.append(result['name'])
        return filteredResults
    
    elif (category in platformLog):
        filteredResults = []
        wantedPlatform = category
        wantedPlatformId = platformLog[wantedPlatform]
        
        if (wantedPlatform is not ""):
            reqPath = "https://api.igdb.com/v4/games"
            firstData = 'fields name, platforms; where platforms = ' + str(wantedPlatformId) + ';'
            b = requests.post(reqPath, data=firstData, headers=myobj)
            bData = b.json()

        for result in bData:
            filteredResults.append(result['name'])
        return filteredResults
    
    else:
        filteredResults = []
        wantedPlatform = category
        wantedPlatformId = category
 
        reqPath = "https://api.igdb.com/v4/games"
        firstData = 'fields name, age_ratings.rating; where age_ratings.rating = ' + category + ';'
        print(firstData)
        b = requests.post(reqPath, data=firstData, headers=myobj)
        bData = b.json()
        print(bData)

        for result in bData:
            filteredResults.append(result['name'])
        return filteredResults

################################################################################