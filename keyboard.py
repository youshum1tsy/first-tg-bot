from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

KBstart = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
KBdesc = ReplyKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True)
KBhelp = ReplyKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True)
B_help = KeyboardButton(text='/help')
B_desc = KeyboardButton(text='/description')
B_menu = KeyboardButton(text='/menu')

KBstart.add(B_help,B_desc,B_menu)
KBdesc.add(B_menu,B_help)
KBhelp.add(B_desc,B_menu)

IKBmenu = InlineKeyboardMarkup()
IKBbackmenu = InlineKeyboardMarkup()
IKBbackmenuphoto = InlineKeyboardMarkup()
IKBbackmenulocation = InlineKeyboardMarkup()
IKBbackmenusticker = InlineKeyboardMarkup()

IB_menu = InlineKeyboardButton(text='back to menu',
                               callback_data='/backtomenu')

IB_help = InlineKeyboardButton(text='help',
                               callback_data='/help')

IB_desc = InlineKeyboardButton(text='description',
                               callback_data='/description')

IB_image = InlineKeyboardButton(text='image',
                                callback_data='/image')

IB_like = InlineKeyboardButton(text='❤️',
                               callback_data='/like')

IB_dislike = InlineKeyboardButton(text='💔',
                                  callback_data='/dislike')

IB_location = InlineKeyboardButton(text='location',
                                   callback_data='/location')

IB_sticker = InlineKeyboardButton(text='sticker',
                                  callback_data='/sticker')

IKBmenu.add(IB_help,IB_desc,).add(IB_image,IB_location).add(IB_sticker)
IKBbackmenu.add(IB_menu)
IKBbackmenuphoto.add(IB_like,IB_dislike).add(IB_image).add(IB_menu)
IKBbackmenulocation.add(IB_location).add(IB_menu)
IKBbackmenusticker.add(IB_sticker).add(IB_menu)