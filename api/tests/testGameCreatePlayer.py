from game import CreatePlayer

class Test_GameCreatePlayer:

    def test_createPlayerConstructor(self):
        p = CreatePlayer('justin', 'key')

        assert p.playerId == '1dd8752235b0f14436f3940d4df5cae4'
        assert p.playerName == 'justin'
        assert len(p.cards) == 0
        assert p.status == 0
