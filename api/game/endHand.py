import bowlRedis

class EndHand:

    def __init__(self, gameId = 0, playerId = None):
        self.gameId = gameId
        self.playerId = playerId

    def End(self, playerId = None):
        return EndHand(gameId=self.gameId,playerId=playerId)

    def Exec(self):
        r = bowlRedis.EndHand()
        r.Init(self)
        
        if r.Exec():
            return self.playerId
