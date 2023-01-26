from aiogram import Bot, Dispatcher, executor, types
from random import randrange, choice
from config import TOKEN
from keyboard import KBstart, KBdesc, KBhelp, IKBmenu, IKBbackmenu, IKBbackmenuphoto, IKBbackmenulocation, IKBbackmenusticker

IMAGE_URL = ['https://clck.ru/33M2W3',
             'https://clck.ru/33M2Xw',
             'https://clck.ru/33M2YD',
             'https://clck.ru/33M2Yw',
             'https://clck.ru/33M2ZH']

STICKER_ID = ['CAACAgIAAxkBAAIUd2PSwE9c_LNlcGDqHUQBpR6kiMy2AAIiJAACmNexSeddSftfsT1ILQQ',
              'CAACAgIAAxkBAAIUemPSwH51Q5Ry3sSjx2AeL23rRumbAAJfGQACTUDgSwmLGJ9rcdVoLQQ',
              'CAACAgIAAxkBAAIUfWPSwKJmk2GK2CbbjZLyOjbITMWXAAJWEgACsm7wS7vnyfIAAfe-5y0E',
              'CAACAgIAAxkBAAIUgGPSwKwjh873dXVrzp-eEAABgd-pWQACcRwAArHxwEvnCgbytSfJfy0E',
              'CAACAgIAAxkBAAIUg2PSwMB6nsdB7lJ1WMl6zKFQv7K0AAJpHgACHe1hSSl1ko95EAL-LQQ']

bot = Bot(TOKEN)
dp = Dispatcher(bot)

STARTING = 'Привет. Я <b>Райя-Прайм</b> - лучшая <b>П.Е.Р.С.И.К</b> во Вселенной!'
HELPING = ''' 
Мои <b>команды</b>:
<b>/menu</b> - <em>Меню взаимодействия со мной.</em>
<b>/help</b> - <em>Вызвать список моих команд.</em>
<b>/description</b> - <em>Мое описание.</em>
<b>/image</b> - <em>Отправлю вам рандомную картинку.</em>
<b>/sticker</b> - <em>Отправлю вам рандомный стикер</em>
<b>/location</b> - <em>Отправлю вам рандомную локацию</em>
'''
DESC = '''Я <b>прикольный</b> <em>пупсик</em>!!!'''

@dp.message_handler(commands=['start','menu'])
async def start_command(message: types.Message):
    if message.text == '/start':
        await bot.send_message(chat_id=message.from_user.id,
                               text=STARTING,
                               parse_mode='HTML',
                               reply_markup=KBstart)
    if message.text == '/menu':
        await bot.send_message(chat_id=message.from_user.id,
                               text='Вы попали в меню!',
                               reply_markup=IKBmenu)

@dp.callback_query_handler()
async def callback_message(callback: types.CallbackQuery,):
    if callback.data == '/help':
        await callback.message.answer(text=HELPING,
                                      parse_mode='HTML',
                                      reply_markup=IKBbackmenu)
    if callback.data == '/description':
        await callback.message.answer(text=DESC,
                                      parse_mode='HTML',
                                      reply_markup=IKBbackmenu)
    if callback.data == '/image':
        await callback.message.answer_photo(photo=choice(IMAGE_URL),
                                            caption='Попробуйте собрать все <b>5</b> фотографий!',
                                            parse_mode='HTML',
                                            reply_markup=IKBbackmenuphoto)
    if callback.data == '/backtomenu':
        await callback.message.answer(text='Вы вернулись в меню!',
                                      reply_markup=IKBmenu)
    if callback.data == '/like':
        await callback.answer(text='Я рад что тебе понравилась данная фотография!')

    if callback.data == '/dislike':
        await callback.answer(text='Надеюсь оставшиеся фотографии тебе понравятся!')

    if callback.data == '/location':
        await callback.message.answer_location(latitude=randrange(0,91),
                                               longitude=randrange(0,181),
                                               reply_markup=IKBbackmenulocation)
    if callback.data == '/sticker':
        await callback.message.answer_sticker(sticker=choice(STICKER_ID),
                                              reply_markup=IKBbackmenusticker)

@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELPING,
                           parse_mode='HTML',
                           reply_markup=KBhelp)

@dp.message_handler(commands='description')
async def desc_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=DESC,
                           parse_mode='HTML',
                           reply_markup=KBdesc)

@dp.message_handler(commands=['image'])
async def random_photo(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=choice(IMAGE_URL))

@dp.message_handler(commands='location')
async def loc_command(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=randrange(0,91),
                            longitude=randrange(0,181))

@dp.message_handler(commands='sticker')
async def random_sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=choice(STICKER_ID),)

async def on_startup(_):
    print('СЭР, Я ГОТОВ РАБОТАТЬ!!!')

if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_startup,skip_updates=True)