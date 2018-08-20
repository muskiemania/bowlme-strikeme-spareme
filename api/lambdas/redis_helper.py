import json

def lambda_handler(event, context):

    #check for input parameters - return dict of keynames

    game_id = None
    player_id = None

    return {
        'gameIdCounter': 'game-id-counter',
        'lastUpdated': 'game-last-updated',
        'allHashes': 'all-game-hashes',
        'game': {
            'gameId': game_id or None,
            'host': {
                'playerName': 'host-name',
                'playerId': 'host-id'
            },
            'deck': game_id and 'game-%s-deck' % game_id or None,
            'discard': game_id and 'game-%s-discard' % game_id or None,
            'players': {
                'players': game_id and 'game-%s-players' % game_id or None,
                'info': game_id and 'game-%s-players-info' % game_id or None,
                'name': player_id and '%s-name' % player_id or None,
                'status': player_id and '%s-status' % player_id or None,
                'rating': player_id and 'player-%s-rating' % player_id or None,
                'rank': player_id and 'player-%s-rank' % player_id or None,
                'hand': game_id and player_id and 'game-%s-player-hand-%s' % (game_id, player_id) or None
            },
            'playerStatuses': game_id and 'game-%s-player-statuses' % game_id or None,
            'lastUpdated': game_id and 'g%s-updated' % game_id or None,
            'gameStatuses': game_id and 'g%s-status' % game_id or None
        }
    }

print json.dumps(lambda_handler(None, None))
