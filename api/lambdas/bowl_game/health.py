import os

class Health(object):

    def __init__(self):
        pass

    @staticmethod
    def check():

        test_env = os.environ or {'nothing': 'there'}

        return {
            'hello': 'There',
            'env': test_env
        }
