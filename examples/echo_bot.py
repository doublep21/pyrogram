from pyrogram import Client, Filters

"""This simple echo bot replies to every private text message"""

app = Client("my_account")


@app.on_message(Filters.text & Filters.private)
def echo(client, message):
    client.send_message(
        message.chat.id, message.text,
        reply_to_message_id=message.message_id
    )


app.start()
app.idle()
