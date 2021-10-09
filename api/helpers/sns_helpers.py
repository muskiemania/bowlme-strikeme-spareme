import boto3

class SnsHelpers:

    @staticmethod
    def publish(**kwargs):
        _arn = kwargs.get('TargetArn')
        _message = kwargs.get('Message')
        _attributes = kwargs.get('MessageAttributes')

        sns = boto3.resource('sns')
        topic = sns.Topic(_arn)

        response = topic.publish(
            Message=json.dumps(_message),
            MessageAttributes=_attributes
        )

        return 'OK'
