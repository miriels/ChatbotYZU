from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='message_korsel',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.its.ac.id/international/wp-content/uploads/sites/66/2019/09/Yzu.jpg',
                    title='About YZU',
                    text=' ',
                    actions=[
                        URITemplateAction(
                            label='How to get YZU',
                            uri='https://www.yzu.edu.tw/aboutyzu/index.php/en-us/campus-tour/how-to-get-to-yzu'
                        ),
                        URITemplateAction(
                            label='Yuan Ze 360 Virtual Tour',
                            uri='http://underadmissions.yzu.edu.tw/enroll/new/virtual_tours/'
                        ),
                        URITemplateAction(
                            label='Campus Photo',
                            uri='https://www.yzu.edu.tw/aboutyzu/index.php/en-us/campus-tour/campus-photo'
                        )
                    ]
                )
            ]
        )
    )
    return message