from utils.permissions import is_admin

warn_data = {}

def register(bot):
    @bot.message_handler(commands=["warn"])
    def warn(message):
        if not is_admin(bot, message): return
        if not message.reply_to_message:
            bot.reply_to(message, "Uyarı için bir mesaja yanıt ver.")
            return
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        warn_data.setdefault(chat_id, {})
        warn_data[chat_id][user_id] = warn_data[chat_id].get(user_id, 0) + 1
        bot.reply_to(message, f"Uyarı verildi. Toplam uyarı: {warn_data[chat_id][user_id]}")

    @bot.message_handler(commands=["infractions"])
    def show_warns(message):
        if not is_admin(bot, message): return
        if not message.reply_to_message:
            bot.reply_to(message, "Kullanıcıya yanıtla.")
            return
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        total = warn_data.get(chat_id, {}).get(user_id, 0)
        bot.reply_to(message, f"Toplam uyarı: {total}")
