from config import GIRIS_MESAJI

def register(bot):
    @bot.message_handler(content_types=["new_chat_members"])
    def welcome_new_member(message):
        for user in message.new_chat_members:
            name = user.first_name
            bot.send_message(message.chat.id, GIRIS_MESAJI.format(name=name))
