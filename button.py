import requests
import os

TOKEN = os.environ['TOKEN']

def Button(chat_id:str, photo:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

    ButtonText1 = {'text':'🌠Dizayn darslar'}
    ButtonText2 = {'text':'👨🏻‍💻Dasturlash darslari'}
    ButtonText3 = {'text':'🙋🏻‍♂️Frilanserlik darslari'}
    ButtonText4 = {'text':'🖥️Kompyuter Bilimlari'}
    ButtonText5 = {'text':'🧩IT nima?'}
    ButtonText6 = {'text':'📌Loyiha maqsadi'}
    ButtonText7 = {'text': "📞Biz bilan bog'lanish"}
    reply_markup = {
        'keyboard':[
            [ButtonText1,ButtonText2],
            [ButtonText3,ButtonText4],
            [ButtonText5],
            [ButtonText6, ButtonText7]
        ]}
    payload = {
        'chat_id':chat_id,
        'photo':photo,
        'reply_markup':reply_markup
    }

    r = requests.get(url=URL, json=payload)
chat_id = '996172963'
photo = 'https://random.dog/2d394360-33e1-4c27-9e64-d65a2ab82d5b.jpg'
Button(chat_id=chat_id, photo=photo)