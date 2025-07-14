from utils.permissions import is_admin
import telebot

def register(bot):
    @bot.message_handler(commands=["ban"])
    def ban_user(message):
        if not is_admin(bot, message): return
        if not message.reply_to_message:
            bot.reply_to(message, "Banlamak için bir mesaja yanıt ver.")
            return
        try:
            bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.reply_to(message, "Kullanıcı banlandı.")
        except:
            bot.reply_to(message, "Ban başarısız.")

    @bot.message_handler(commands=["kick"])
    def kick_user(message):
        if not is_admin(bot, message): return
        if not message.reply_to_message:
            bot.reply_to(message, "Atmak için bir mesaja yanıt ver.")
            return
        try:
            bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.reply_to(message, "Kullanıcı atıldı.")
        except:
            bot.reply_to(message, "Atma başarısız.")

    @bot.message_handler(commands=["mute"])
    def mute_user(message):
        if not is_admin(bot, message): return
        if not message.reply_to_message:
            bot.reply_to(message, "Susturmak için mesaj yanıtla.")
            return
        bot.restrict_chat_member(
            message.chat.id,
            message.reply_to_message.from_user.id,
            permissions=telebot.types.ChatPermissions(can_send_messages=False)
        )
        bot.reply_to(message, "Kullanıcı susturuldu.")

    @bot.message_handler(commands=["unmute"])
    def unmute_user(message):
        if not is_admin(bot, message): return
        if not message.reply_to_message:
            bot.reply_to(message, "Mesaj yanıtla.")
            return
        bot.restrict_chat_member(
            message.chat.id,
            message.reply_to_message.from_user.id,
            permissions=telebot.types.ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True
            )
        )
        bot.reply_to(message, "Kullanıcının sesi açıldı.")
