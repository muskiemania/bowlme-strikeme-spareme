import json
import bowl_game

def lambda_handler(event, context):

    return json.dumps(bowl_game.Health.check())
