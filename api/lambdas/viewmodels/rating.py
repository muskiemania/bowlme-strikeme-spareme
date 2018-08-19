
class RatingModel(object):
    def __init__(self, rating):
        self.rating = rating

    def fromDto(self):
        #rating is a tuple(strength int, card1, card2, card3, card4, card5, name)
        #return {'description': self.rating.get()[6]}
        return {'description': self.rating.get()[6], 'rank': self.rating.rank}
