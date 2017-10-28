class RedisKeys(object):
    def __init__(self, game_id=None, player_id=None):
        self.game_id = game_id
        self.player_id = player_id

    def game_id_counter(self):
        return 'game-id-counter'

    def game_info(self):
        if self.game_id is None:
            raise Exception('no game_id')
        return 'game-%s-info' % self.game_id

    def game_info_host_name_key(self):
        return 'host_name'

    def game_info_host_id_key(self):
        return 'host_id'

    def game_info_status_key(self):
        return 'status'
    
    def game_deck(self):
        if self.game_id is None:
            raise Exception('no game_id')
        return 'game-%s-deck' % self.game_id

    def game_discard(self):
        if self.game_id is None:
            raise Exception('no game_id')
        return 'game-%s-discard' % self.game_id

    def game_players(self):
        if self.game_id is None:
            raise Exception('no game_id')
        return 'game-%s-players' % self.game_id

    def game_players_info(self):
        if self.game_id is None:
            raise Exception('no game_id')
        return 'game-%s-players-info' % self.game_id

    def game_players_name_key(self):
        if self.player_id is None:
            raise Exception('no player_id')
        return '%s-name' % self.player_id

    def game_players_status_key(self):
        if self.player_id is None:
            raise Exception('no player_id')
        return '%s-status' % self.player_id

    def game_players_rating(self):
        if self.player_id is None:
            raise Exception('no player_id')
        return 'player-%s-rating' % self.player_id

    def game_players_rank(self):
        if self.player_id is None:
            raise Exception('no player_id')
        return 'player-%s-rank' % self.player_id

    def game_player_statuses(self):
        if self.game_id is None:
            raise Exception('no game_id')
        return 'game-%s-player_statuses' % self.game_id

    def game_player_hand(self):
        if self.game_id is None:
            raise Exception('no game_id')
        if self.player_id is None:
            raise Exception('no player_id')
        return 'game-%s-player_hand-%s' % (self.game_id, self.player_id)

    def game_last_updated(self):
        return 'game-last-updated'

    def game_last_updated_key(self):
        if self.game_id is None:
            raise Exception('no game_id')
        return 'g%s_updated' % self.game_id

    def game_last_updated_status_key(self):
        if self.game_id is None:
            raise Exception('no game_id')
        return 'g%s_status' % self.game_id

    def game_hashes_key(self):
        return 'all_game_hashes'
