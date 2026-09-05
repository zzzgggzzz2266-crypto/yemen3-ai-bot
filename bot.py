import telebot
import google.generativeai as genai
import sys

print("====================================")
print("Yemen AI Bot")
print("مبرمج بواسطة: محمد الحذيفي")
print("====================================")

# المفاتيح
BOT_TOKEN = "8693841076:AAHx4WSEbBzXyt0x6q9KLGxfM5vOth7D12Y"
GEMINI_API_KEY = "AQ.Ab8RN6JQAyo9n5ph1nYKRJhZZyYCAd8ALJ0IzYZMrte9pboGrg"

print(f"BOT_TOKEN موجود: {BOT_TOKEN is not None}")
print(f"GEMINI_API_KEY موجود: {GEMINI_API_KEY is not None}")

try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    bot = telebot.TeleBot(BOT_TOKEN)
    print("تم الاتصال بجيميني وتيليجرام بنجاح")
except Exception as e:
    print(f"ERROR connecting: {e}")
    sys.exit(1)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "اهلا! انا بوت يمني AI 🔥\nمبرمج بواسطة: محمد الحذيفي")

@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, "هذا البوت مبرمج بواسطة: محمد الحذيفي\nشغال على Gemini 1.5 Flash + Railway 24 ساعة")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"ERROR: {e}")
        bot.reply_to(message, f"صار خطأ: {e}")

print("Polling started... البوت شغال")
bot.polling()