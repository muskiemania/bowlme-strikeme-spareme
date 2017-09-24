from jose import jwt

class Helpers(object):

    def __init__(self):
        self.__cookie_name = 'bowl-strike-spare-cookie'
        self.__jwt_secret = 'bowl-strike-spare-secret'

    def get_cookie_name(self):
        return self.__cookie_name

    def get_jwt(self, data):
        return jwt.encode(data, self.__jwt_secret, algorithm='HS256')

    def decode_jwt(self, token):
        decoded = jwt.decode(token, self.__jwt_secret, algorithms=['HS256'])
        return { str(key):value for key,value in decoded.items() }
    
