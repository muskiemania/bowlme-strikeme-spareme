import base64
import io
from PIL import Image, ImageDraw, ImageColor, ImageFilter
import random

def draw_lanes(image_height=9.0, image_width=2.1, image_dpi=100):

    _COLORS = [
        '#c07f4d',
        '#cc8a57',
        '#d99562',
        '#e5a06c',
        '#f1ab77',
        '#feb781',
        '#ffc28c',
        '#e5a06c',
        '#dda276',
        '#d4a381',
        '#caa58b',
        '#e5a06c',
        '#ecaf84',
        '#f1bf9c',
        '#f6cfb4',
        '#e5a06c',
        '#bb835a'
    ]

    # size of a bowling lane is 42 inches x 75 feet
    # 7.5 feet to dots
    # 15-17 feet for arrows
    # feet 45-60 for registration marks
    # pins from 60-75 feet

    # 42 inches wide
    # 39 boards

    # 42/39 ==> 1 + 3/39 ==> 1 + 1/13 ==> 14/13 * 39

    # if iphone height is 1080px, lets use 900px as our canvas height
    # if 900px == 75 ft, that is 12px per foot, which means 42 px for 42 inches
    # if we use 4 : 1 aspect, then 168 px 

    _lane = Image.new('RGB', (int(image_width * image_dpi), int(image_height * image_dpi)), (255, 255, 255))
    draw = ImageDraw.Draw(_lane)

    start_x = 0
    start_y = 0

    #_lane.save('lane.png')

    for i in range(40):
        if i == 0:
            continue

        random_color = ImageColor.getcolor(random.choice(_COLORS), "RGB")

        _diff = 5

        if i in [1,4,6,9,11,14,16,20,24,26,29,31,34,36,39]:
            _diff = 6

        draw.rectangle([(start_x, start_y), (start_x + _diff - 1, int(image_height * image_dpi))], fill=random_color)
        start_x += _diff


    blurred_image = _lane.filter(ImageFilter.BLUR)
    #blurred_image.save('lane.png')
    blurred_image = Image.alpha_composite(
        Image.new('RGBA', blurred_image.size),
        blurred_image.convert('RGBA')
    )

    image_buffer = io.BytesIO()
    blurred_image.save(image_buffer, format='png')

    image_buffer.seek(0)
    image_bytes_base64 = base64.b64encode(image_buffer.getvalue())
    
    return image_bytes_base64.decode('utf-8')



#diagram = Image.open('sample.png')


#diagram = diagram.transpose(Image.ROTATE_90)

#diagram.show()

#print(diagram.size)
#blurred_image.paste(diagram, (0, 0), diagram)

#blurred_image.show()

#blurred_image.save('lane.png')

