from dynamos.draw_cards import DrawCards as Draw
#from dynamos.player_status import PlayerStatus

class DrawCards:

    @staticmethod
    def draw(game_id, player_id, number_of_cards):
        
        # get cards from deck
        (hand_size, deck_size) = Draw.execute(game_id, player_id, number_of_cards)

        #if stack <= 7:
        #    helpers.SnsHelpers.publish('')

        # adjust player status accordingly
        #if number_of_cards in [3, 4] and hand_size <= 5:
        #    PlayerStatus.finished(game_id, player_id)
        
        #if number_of_cards in [6] and hand_size >= 5:
        #    PlayerStatus.must_discard(game_id, player_id, True)

        #if number_of_cards not in [3, 4, 6] and hand_size >=5:
        #    PlayerStatus.must_discard(game_id, player_id, False)

        return True

