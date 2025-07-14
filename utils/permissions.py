def is_admin(bot, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    member = bot.get_chat_member(chat_id, user_id)
    if member.status in ["administrator", "creator"]:
        return True
    else:
        bot.reply_to(message, "❌ Bu komutu sadece yöneticiler kullanabilir.")
        return False
