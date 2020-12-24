from models.model import User, Listing, Booking, Transaction, Support, Booking, Chat, Review
from bson.objectid import ObjectId
from PIL import Image
import base64
import pymongo
from io import BytesIO
buffered = BytesIO()

client = pymongo.MongoClient('mongodb+srv://admin:slapbass@cluster0.a6um0.mongodb.net/test')['Tourisit']

# tour_name = 'Best of Kampong Glam'
# tour_brief= 'Walk around this architectural marvel that™s both a cultural attraction and a historical museum'
# tour_desc = 'Swing by Kampong Gelam, Singapore™s oldest quarter, to get to know the culture and traditions of the Malay community and Islam. Discover the origins of the old Royal Palace and Sultan Mosque. You"ll also be taught how to tie a sarong (a large length of fabric often wrapped around the waist and worn by men and women throughout most of Indonesia). Don™t miss Haji Lane, one of Singapore™s most popular streets known for its cool backdrops and quirky shops.'
# tour_price = 70
# tg_uid = '5fde1b5bdf4fe3bc527058f1'
# tour_img = 'hi'

db = client['Listings']

x = list(db.find())
for i in x:
    print(i['_id'])


def img_to_base64(img):
    img = Image.open(img).resize((150, 150))
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str


# co = True
# while co:
#     tour_name = input('Name:')
#     tour_brief = input('Tour brief:')
#     tour_desc = input('Tour Desc')
#     tour_price = input('Tour price')
#     tg_uid = '5fde1b5bdf4fe3bc527058f1'
#     tour_img = img_to_base64('../public/imgs/bookings.jpg')
#     x = Listing(tour_name, tour_brief, tour_desc, tour_price, tg_uid, tour_img)
#     y = x.return_obj()
#     db = client['Listings']
#     db.insert_one(y)
#     cont = input('cont?:')
#     if cont == 'f':
#         co = False


# db = client['Listings']
# x = list(db.find())
# print(x[0]['tour_brief'])
# # USERS
# x = User('Jake', 'getbass', 'ejrkrej2JKEKRJEKJR.@JREIJROM')
# y = x.return_obj()
# print(y)
# db = client['Users']
# db.insert_one(y)

# LISTINGS
# img_str = img_to_base64('public/imgs/bookings.jpg')
# x = Listings('Gay bars', 'THis is not me', '60', 'iire3', tour_img=img_str)
# y = x.return_obj()
# print(y)
# db = client['Listings']
# db.insert_one(y)
