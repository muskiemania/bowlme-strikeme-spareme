import bowl_game

def lambda_handler(event, context):

    return bowl_game.Health.check()
