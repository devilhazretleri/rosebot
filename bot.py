import telebot
from config import TOKEN
from handlers import moderation, welcome, filters, cleaner, warnings, buttons

bot = telebot.TeleBot(TOKEN)

moderation.register(bot)
welcome.register(bot)
filters.register(bot)
cleaner.register(bot)
warnings.register(bot)
buttons.register(bot)

print("Bot aktif!")
bot.infinity_polling()
