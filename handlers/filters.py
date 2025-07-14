from config import KUFUR_KELIMELERI

def register(bot):
    @bot.message_handler(func=lambda m: True, content_types=['text'])
    def kufur_engelle(message):
        text = message.text.lower()
        if any(kufur in text for kufur in KUFUR_KELIMELERI):
            try:
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id, f"{message.from_user.first_name}, küfür yasak!")
            except:
                pass
        if "http://" in text or "https://" in text or "t.me/" in text:
            try:
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id, f"{message.from_user.first_name}, bağlantı paylaşmak yasak!")
            except:
                pass
