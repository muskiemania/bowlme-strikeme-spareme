from lambdas import game

def lambda_handler(event, context):

    #fetch input...
    game_id = event['gameId']
    number_of_decks = event['numberOfDecks'] or 1

    #create deck(s)
    decks = game.CreateDeck.create(game_id, number_of_decks)

    return decks.json()
