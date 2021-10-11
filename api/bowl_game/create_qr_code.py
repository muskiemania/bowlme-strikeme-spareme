import pyqrcode
import boto3

class CreateQrCode:

    @staticmethod
    def create(game_id):

        # create qr code as svg
        material = pyqrcode.create(f'some qr code material here: {game_id}')
        _buffer = io.BytesIO()
        material.svg(_buffer, scale=4, module_color='white', quiet_zone=2)

        # write to s3 bucket
        _buffer.seek(0)
        s3 = boto3.resource('s3', region_name='us-east-1')
        bucket = s3.Bucket('bowl.muskiemania.net')
        bucket.put_object(
            Body=_buffer,
            ContentType='image/svg',
            Key=f'static/qr/{game_id}.svg'
        )

        return True
