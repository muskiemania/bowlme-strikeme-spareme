from lambdas import game

def lambda_handler(event, context):

    #fetch input...
    game_id = event['gameId']

    #create game
    shuffled_deck = game.ShuffleDeck.shuffle(game_id)

    return shuffled_deck.json()
