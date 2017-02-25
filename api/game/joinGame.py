from createPlayer import CreatePlayer
import bowlRedis

class JoinGame:

    def __init__(self, gameId = 0, player = None):
        self.gameId = gameId
        self.player = player

    def Join(self, playerName = None):
        player = CreatePlayer(playerName, self.gameId)        

        return JoinGame(gameId=self.gameId,player=player)

    def Exec(self):
        r = bowlRedis.JoinGame()
        r.Init(self)
        
        if r.Exec():
            return self.player.playerId
