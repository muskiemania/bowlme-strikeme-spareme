import hashlib

class CreatePlayer:

    def __init__(self, player_name, game_id):
        md5 = hashlib.md5()
        md5.update(player_name)
        md5.update(game_id)
        player_id = md5.hexdigest()
        
        self.player_id = player_id
        self.player_name = player_name
        self.cards = []
        self.status = 0
