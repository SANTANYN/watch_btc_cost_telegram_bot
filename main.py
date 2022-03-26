import requests
import telebot
from datetime import datetime
from auth_data import auth_token


def get_data():
    get_req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = get_req.json()
    print(response)
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%y-%m-%d %H:%M')}\nSell BTC price: {sell_price} USD!")

def telegram_bot(auth_token):
    bot = telebot.TeleBot(auth_token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! Write the 'price' to find out the cost BTC!")

    @bot.message_handler(content_types=["text"])
    def send_message(message):
        if message.text.lower() == 'price':
            try:
                get_req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = get_req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%y-%m-%d %H:%M')}\nSell BTC price: {sell_price} USD!"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn... Something was wrong"
                )
        else:
            bot.send_message(message.chat.id, "Whaaat? check the command dude!")



    bot.polling()

if __name__ == "__main__":
    get_data()
    telegram_bot(auth_token)