import jwt

def handler(event, context):

    # first need to check the token
    _token = event['authorizationToken']

    try:
        decoded = jwt.decode(_token, 'secret', algorithms=['HS256'])
        principal_id = decoded['sub']
        policy_document = {
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Action': 'execute-api:Invoke',
                        'Effect': 'Allow',
                        'Resource': event['methodArn']}]}
        context = {
                'gameId': decoded['aud'],
                'playerId': decoded['sub'],
                'playerName': decoded['name']}
    except:
        principal_id = 'unauthorized'
        policy_document = {
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Action': 'execute-api:Invoke',
                        'Effect': 'Deny',
                        'Resource': event['methodArn']}]}
        context = {}
    
    return {
            'principalId': principal_id,
            'policyDocument': policy_document,
            'context': context}


    # then need to extract key user info

    # then need to create the policy
