import bowlRedis

class StartGame:

    def __init__(self, gameId = 0, playerId = None):
        self.gameId = gameId
        self.playerId = playerId

    def Start(self, playerId = None):
        return StartGame(gameId=self.gameId,playerId=playerId)

    def Exec(self):
        r = bowlRedis.StartGame()
        r.Init(self)
        
        if r.Exec():
            return self.gameId
