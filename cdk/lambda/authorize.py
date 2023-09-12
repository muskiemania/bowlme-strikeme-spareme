import jwt
import traceback

def handler(event, context):

    print(event)

    # first need to check the token
    _token = event.get('headers', {})['authorization']
    _token = _token.split(' ')[1]

    try:
        decoded = jwt.decode(_token, 'secret', audience='BOWL_API', algorithms=['HS256'])
        principal_id = decoded['sub'].split(' ')[1]
        policy_document = {
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Action': 'execute-api:Invoke',
                        'Effect': 'Allow',
                        'Resource': event['methodArn']}]}
        context = {
                'gameId': decoded['sub'].split(' ')[0],
                'playerId': decoded['sub'].split(' ')[1],
                'playerName': decoded['name']}
    except:
        traceback.print_exc()

        principal_id = 'unauthorized'
        policy_document = {
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Action': 'execute-api:Invoke',
                        'Effect': 'Deny',
                        'Resource': event['routeArn']}]}
        context = {}
    
    policy = {
            'principalId': principal_id,
            'policyDocument': policy_document,
            'context': context}

    print(policy)
    return policy

    # then need to extract key user info

    # then need to create the policy
