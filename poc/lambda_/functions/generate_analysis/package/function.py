import base64
import boto3
import io
import json
import os
from PIL import Image

from .helpers.analysis_helper import draw_analysis
from .helpers.image_helper import draw_lanes
from .helpers.scipy_helper import interpolate

def handler(event, context):

    # start with the series_id, game_number, and throw id
    _series_id = event.get('series_id')
    _game_number = event.get('game_number')
    _id = event.get('id')
    # event will also have all of the data

    _data = {}

    '''
    def draw_analysis(image_height=9.0, image_width=2.1, image_dpi=100, start_x=None, start=None, slide=None, dots=None, arrows=None, break_point=None, break_location=None, pin_entry=None, pin_exit=None):
    '''


    if 'start_distance' in event.get('data', {}):
        _data['start_x'] = -1 * abs(int(event.get('data', {}).get('start_distance')))

    for each in ['start', 'slide', 'arrows', 'break_point', 'break_distance', 'pin_entry', 'pin_exit']:

        if each in event.get('data', {}):
            _data[each] = abs(int(event.get('data', {}).get(each)))

    # prep for matplotlib
    os.makedirs('/tmp/matplotlib', exist_ok=True)

    spline = interpolate(_data)

    print('spline data is:')
    print(spline)

    _data['spline'] = spline

    # returns base64-encoded byte-string
    encoded_overlay = draw_analysis(9.0, 2.1, **_data)

    # returnes base64-encoded byte-string
    encoded_lanes = draw_lanes(9.0, 2.1)

    # decode bytes strings
    # merge images, create bytes
    overlay_bytes = base64.b64decode(encoded_overlay)
    lanes_bytes = base64.b64decode(encoded_lanes)

    overlay = Image.open(io.BytesIO(overlay_bytes))
    overlay = overlay.transpose(Image.ROTATE_90)

    lanes = Image.open(io.BytesIO(lanes_bytes))
    lanes.paste(overlay, (0, 0), overlay)

    analysis_graphic_bytes = io.BytesIO()
    lanes.save(analysis_graphic_bytes, format='png')
    analysis_graphic_bytes.seek(0)

    # write object to s3
    _metadata = json.loads(os.environ.get('S3', {}))
    _bucket = _metadata.get('bowling-analysis-bucket', {})

    s3 = boto3.client('s3')
    s3.put_object(
        Body=analysis_graphic_bytes,
        Bucket=_bucket.get('bucket_name'),
        Key=f'muskiemania/{_series_id}_{str(_game_number)}_{_id}.png'
    )

    


