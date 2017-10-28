
class RatingDto(object):
    def __init__(self, rating):
        self.__delimiter = '#'
        print rating
        if type(rating) is tuple:
            self.__rating = rating
        if type(rating) is list:
            self.__rating = tuple(rating)
        if type(rating) is str:
            string_rating = rating.split('#')
            for i in range(0, len(string_rating)-2):
                string_rating[i] = int(string_rating[i])
                
            self.__rating = tuple(string_rating)

        print str(type(rating))
        print self.__rating
            
    def get(self):
        return self.__rating

    def as_string(self):
        string_rating = map(lambda x: str(x), list(self.__rating))            
        return self.__delimiter.join(string_rating)
