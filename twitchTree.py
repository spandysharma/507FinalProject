'''This is a demo file to demonstrate how my data handling would
have looked like if I had been able to access the Twitch Popularity API'''

class Game:
    
    def __init__(self, gameID, eligibleStreamers, eligibleViewers, numInstalls, similarGames):
        self.key = gameID # each node in the tree should have a unique ID
        self.streamers = eligibleStreamers # number of people who streamed videos related to the game
        self.viewers = eligibleViewers # number of people who viewed the game
        self.downloads = numInstalls # number of people who installed/downloaded the game
        self.similarGames = similarGames # games similar to the current game. I would have used my exisiting
                                         # IGDB API to get this as it has an endpoint similar_games
                                         # array of game object

'''ATTEMPT FOR USING TWITCH API TO GET EACH GAME'S POPULARITY'''

'''
reqPath = "https://api.igdb.com/v4/games"
# reqPath = "https://api.igdb.com/v4/platforms"
firstData = 'fields name, age_ratings.rating; where age_ratings.rating = 8;'
b = requests.post(reqPath, data=firstData, headers=myobj)
bData = b.json()
print("bData=====================",bData)

def getPopularity(category):
    gameList = searchByCategory(category)
    for name in gameList:
        pass # for now

newAccess = "https://id.twitch.tv/oauth2/token?client_id=cjrl47h8vj7xu45bluva17is0fpb0c&client_secret=3b03ng6xwetf5l0zanbzvmkc3wuea2&grant_type=client_credentials"
newAccess = "https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=cjrl47h8vj7xu45bluva17is0fpb0c&redirect_uri=http://localhost:5000&scope=channel%3Amanage%3Apolls+channel%3Aread%3Apolls&state=c3ab8aa609ea11e793ae92361f002671"
a = requests.post(newAccess)
aData = a.json()
print(aData)
newAccessToken = aData["access_token"]
print(newAccessToken)

myobj = \
{"Client-ID": clientId,
"Authorization": "Bearer " + newAccessToken,
"Body": "fields *;"}

newReqPath = "https://api.twitch.tv/helix/analytics/games?game_id=244929"
data = 'fields *;'

b = requests.post(newReqPath, data=data, headers=myobj)
print(b)
bData = b.json()
print(bData)
'''