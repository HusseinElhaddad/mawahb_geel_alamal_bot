import telebot

# === CONFIG ===
TOKEN = "8073950760:AAGIY4T6CtxELWBBHyB3mIZEt2xzXDRu5S8"
CHANNEL_ID = -1003022635968  # your private channel ID

bot = telebot.TeleBot(TOKEN)

# Handle incoming videos or documents (some videos come as documents)
@bot.message_handler(content_types=['video', 'document'])
def handle_video(message):
    try:
        # Forward the student’s message to your channel
        bot.forward_message(CHANNEL_ID, message.chat.id, message.message_id)

        # Acknowledge student
        bot.reply_to(message, "✅ Your video has been received. Thank you!")

    except Exception as e:
        print("Error:", e)
        bot.reply_to(message, "⚠️ Something went wrong. Please try again.")

print("Bot is running... Press Ctrl+C to stop.")
bot.polling(none_stop=True)
