from keep_alive import keep_alive
keep_alive()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import random
import asyncio

print("Bot is running now... ✅")

# ✅ Allowed Users
ALLOWED_USERS = [7676386584, 7774300280]

# 🔑 Bot Token
TOKEN = "8017700197:AAGiUyvlCybRcRN-nkjcutzXmQfSd6ZE7c4"

# 💌 Compliments
compliments = [
    "Tumhari muskurahat dil chura leti hai 🥺✨",
    "Aaj bhi tum pehli baar jitni hi pyaari lag rahi ho 💖",
    "Tum sirf khoobsurat nahi, sabse khaas ho meri duniya mein 🌍❤️",
    "Tere bina din adhura lagta hai 😢",
    "Tu khush rahe, bas yehi dua hai har waqt 🕊️💫"
]

# 📝 Memories
memories = [
    "Yaad hai jab pehli baar tumse baat hui thi? Dil khush ho gaya tha 😌",
    "Jab tum hansi thi, uss din mein jeet gaya tha 💕",
    "Tere saath bitaya har pal ek yaadgar memory ban gaya 🥰",
    "Kabhi kabhi purani chats padhta hu aur smile aa jaati hai 😊"
]

# 🔹 Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_USERS:
        return
    await update.message.reply_text("Hello 👋 Main aapka pyara assistant hu 💖")

async def compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_USERS:
        return
    await update.message.reply_text(random.choice(compliments))

async def memory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_USERS:
        return
    await update.message.reply_text(random.choice(memories))

# 🕒 Scheduled Messages
async def cute_question(context: ContextTypes.DEFAULT_TYPE):
    for user_id in ALLOWED_USERS:
        await context.bot.send_message(chat_id=user_id, text="Aap itni cute kyun ho? 🥹")
        await context.bot.send_message(chat_id=user_id, text="Jatin ko ek daar dena zaroor aaj 😛")

async def daily_greetings(context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now().hour
    if 5 <= now < 12:
        msg = "Good Morning ☀️ Utho aur ek pyara sa smile do 💛"
    elif 12 <= now < 17:
        msg = "Good Afternoon 😇 Paani piya kya? Rest karlo thoda 🧋"
    elif 17 <= now < 21:
        msg = "Good Evening 🌆 Thoda fresh ho jao aur khana time pe khana 🍽️"
    else:
        msg = "Good Night 🌙 Sapno mein Jatin ko zaroor le aana 😅❤️"
    for user_id in ALLOWED_USERS:
        await context.bot.send_message(chat_id=user_id, text=msg)

# 🗓️ Scheduler Setup
scheduler = BackgroundScheduler()
scheduler.add_job(daily_greetings, "interval", hours=6)
scheduler.add_job(cute_question, "interval", hours=4)
scheduler.start()

# 🚀 Main Application
async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("compliment", compliment))
    app.add_handler(CommandHandler("memory", memory))
    await app.run_polling()

asyncio.run(main())
