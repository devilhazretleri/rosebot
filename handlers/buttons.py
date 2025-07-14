from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot

def register(bot):
    @bot.message_handler(commands=["panel"])
    def show_panel(message):
        markup = InlineKeyboardMarkup()
        markup.row(
            InlineKeyboardButton("Ban", callback_data="ban"),
            InlineKeyboardButton("Kick", callback_data="kick")
        )
        markup.row(
            InlineKeyboardButton("Mute", callback_data="mute"),
            InlineKeyboardButton("Unmute", callback_data="unmute")
        )
        bot.send_message(message.chat.id, "⚙️ Yönetici Paneli", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def handle_callbacks(call):
        if not call.message.reply_to_message:
            bot.answer_callback_query(call.id, "Bir kullanıcı mesajına yanıtla.")
            return
        msg = call.message
        user_id = msg.reply_to_message.from_user.id
        chat_id = msg.chat.id

        if call.data == "ban":
            bot.ban_chat_member(chat_id, user_id)
            bot.send_message(chat_id, "Kullanıcı banlandı.")
        elif call.data == "kick":
            bot.kick_chat_member(chat_id, user_id)
            bot.unban_chat_member(chat_id, user_id)
            bot.send_message(chat_id, "Kullanıcı atıldı.")
        elif call.data == "mute":
            bot.restrict_chat_member(
                chat_id,
                user_id,
                permissions=telebot.types.ChatPermissions(can_send_messages=False)
            )
            bot.send_message(chat_id, "Kullanıcı susturuldu.")
        elif call.data == "unmute":
            bot.restrict_chat_member(
                chat_id,
                user_id,
                permissions=telebot.types.ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True
                )
            )
            bot.send_message(chat_id, "Kullanıcının sesi açıldı.")
