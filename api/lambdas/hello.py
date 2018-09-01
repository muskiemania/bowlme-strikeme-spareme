from lambdas.bowl_game import Health

def lambda_handler(event, context):

    return bowl_game.Health.check()
