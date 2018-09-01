import bowl_game

def lambda_handler(event, context):

    #fetch input...
    game_id = event['gameId']

    #create game
    shuffled_deck = bowl_game.ShuffleDeck.shuffle(game_id)

    return shuffled_deck.json()
