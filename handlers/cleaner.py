from utils.permissions import is_admin

def register(bot):
    @bot.message_handler(commands=["sil"])
    def temizle(message):
        if not is_admin(bot, message): return
        try:
            count = int(message.text.split()[1])
            for i in range(count):
                bot.delete_message(message.chat.id, message.message_id - i)
            bot.send_message(message.chat.id, f"{count} mesaj silindi.")
        except:
            bot.reply_to(message, "Kullanım: /sil 10")
