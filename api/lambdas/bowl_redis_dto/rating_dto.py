
class RatingDto(object):
    def __init__(self, rating, player_id=None):
        self.__delimiter = '#'
        #print rating
        if isinstance(rating, tuple):
            self.__rating = rating
        if isinstance(rating, list):
            self.__rating = tuple(rating)
        if isinstance(rating, str):
            string_rating = rating.split('#')
            self.__rating = tuple(string_rating)

        self.player_id = player_id
        self.rank = None
        #print str(type(rating))
        #print self.__rating
            
    def get(self):
        return self.__rating

    def as_string(self):
        string_rating = map(lambda x: str(x), list(self.__rating))            
        return self.__delimiter.join(string_rating)
