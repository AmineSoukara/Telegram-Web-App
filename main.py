import os

from flask import Flask, jsonify, render_template, request
from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from utils import parse_init_data

from config import *

app = Flask(__name__, static_url_path="/static")


API_ID = 2059351
API_HASH = "055ad1774b838870be128567b7a4c04a"
BOT_TOKEN = "5186450665:AAEJjATsJZJvQ0vuoGS0PDHUsdYjFhEv6Ug"

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
bot.start()


@app.get("/")
def index():
    return render_template("index.html")


@app.route("/getMe")
def getMe():
    print("start")
    me = bot.get_me()
    print("end")
    print(me)
    return jsonify(me)


@app.post("/submitOrder")
def submit_order():
    data = request.json
    init_data = parse_init_data(token=BOT_TOKEN, raw_init_data=data["initData"])
    if init_data is False:
        return False

    query_id = init_data["query_id"]

    result_text = "<b>Order summary:</b>\n\n"
    for item in data["items"]:
        name, price, amount = item.values()
        result_text += f"{name} x{amount} — <b>{price}</b>\n"
    result_text += "\n" + data["totalPrice"]

    result = InlineQueryResultArticle(
        id=query_id,
        title="Order",
        input_message_content=InputTextMessageContent(result_text, parse_mode="HTML"),
    )
    bot.answer_web_app_query(query_id, result)
    return ""


@bot.on_message(filters.private & filters.command(["start", "help"]))
def cmd_start(c, m):
    m.reply("done")


if __name__ == "__main__":
    app.run(host=WEBAPP_HOST, port=WEBAPP_PORT)
