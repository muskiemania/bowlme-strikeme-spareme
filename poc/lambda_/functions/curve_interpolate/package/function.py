import json
from .helpers.curve_helper import draw_curve

def handler(event, context):

    # start with the series_id, game_number, and throw id
    # event will also have all of the data

    print('event is:')
    print(event)

    _data = {}

    '''
    def draw_curve(slide=None, dots=None, arrows=None, break_point=None, break_location=None, pin_entry=None):
    '''

    for each in ['slide', 'arrows', 'break_point', 'break_distance', 'pin_entry']:

        if each in event:
            _data[each] = abs(int(event.get(each)))

    spline = draw_curve(**_data)

    print('spline is:')
    print(spline)

    return spline

