import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import datetime
import random
import asyncio

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

print("Bot is starting... ✅")

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

# Global application variable
application = None

# 🔹 Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler"""
    if update.effective_user.id not in ALLOWED_USERS:
        logger.warning(f"Unauthorized access attempt by user {update.effective_user.id}")
        return
    
    await update.message.reply_text("Hello 👋 Main aapka pyara assistant hu 💖")

async def compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random compliment"""
    if update.effective_user.id not in ALLOWED_USERS:
        return
    
    await update.message.reply_text(random.choice(compliments))

async def memory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random memory"""
    if update.effective_user.id not in ALLOWED_USERS:
        return
    
    await update.message.reply_text(random.choice(memories))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show available commands"""
    if update.effective_user.id not in ALLOWED_USERS:
        return
    
    help_text = """
Available commands:
/start - Start the bot
/compliment - Get a sweet compliment
/memory - Get a cherished memory
/help - Show this help message
    """
    await update.message.reply_text(help_text)

# 🕒 Scheduled Message Functions
async def send_cute_question():
    """Send cute question to all allowed users"""
    global application
    if application is None:
        return
        
    for user_id in ALLOWED_USERS:
        try:
            await application.bot.send_message(
                chat_id=user_id, 
                text="Aap itni cute kyun ho? 🥹"
            )
            await asyncio.sleep(1)
            await application.bot.send_message(
                chat_id=user_id, 
                text="Jatin ko ek daar dena zaroor aaj 😛"
            )
        except Exception as e:
            logger.error(f"Error sending cute question to {user_id}: {e}")

async def send_daily_greetings():
    """Send time-appropriate greetings"""
    global application
    if application is None:
        return
        
    # Simple time handling without timezone complications
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
        try:
            await application.bot.send_message(chat_id=user_id, text=msg)
        except Exception as e:
            logger.error(f"Error sending greeting to {user_id}: {e}")

# 🔄 Background Task for Scheduled Messages
async def scheduled_messages():
    """Background task to send scheduled messages"""
    last_greeting_hour = -1
    cute_question_counter = 0
    
    while True:
        try:
            current_hour = datetime.datetime.now().hour
            
            # Send greetings every 6 hours (at 6, 12, 18, 0)
            if current_hour in [6, 12, 18, 0] and current_hour != last_greeting_hour:
                await send_daily_greetings()
                last_greeting_hour = current_hour
                logger.info(f"Sent daily greeting at hour {current_hour}")
            
            # Send cute questions every 4 hours
            cute_question_counter += 1
            if cute_question_counter >= 240:  # 240 minutes = 4 hours
                await send_cute_question()
                cute_question_counter = 0
                logger.info("Sent cute question")
            
            await asyncio.sleep(60)  # Check every minute
            
        except Exception as e:
            logger.error(f"Error in scheduled messages: {e}")
            await asyncio.sleep(60)

# 🚀 Main Application
async def main():
    """Main function to run the bot"""
    global application
    
    try:
        # Create application with minimal configuration
        application = (
            Application.builder()
            .token(TOKEN)
            .build()
        )
        
        # Add command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("compliment", compliment))
        application.add_handler(CommandHandler("memory", memory))
        application.add_handler(CommandHandler("help", help_command))
        
        # Start background task for scheduled messages
        asyncio.create_task(scheduled_messages())
        
        print("Bot is running now... ✅")
        logger.info("Bot started successfully")
        
        # Run the bot with minimal settings
        await application.run_polling(
            drop_pending_updates=True,
            allowed_updates=Update.ALL_TYPES
        )
        
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped by user")
    except Exception as e:
        print(f"Fatal error: {e}")
        logger.error(f"Fatal error: {e}")import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import datetime
import random
import asyncio

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

print("Bot is starting... ✅")

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

# Global application variable
application = None

# 🔹 Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler"""
    if update.effective_user.id not in ALLOWED_USERS:
        logger.warning(f"Unauthorized access attempt by user {update.effective_user.id}")
        return
    
    await update.message.reply_text("Hello 👋 Main aapka pyara assistant hu 💖")

async def compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random compliment"""
    if update.effective_user.id not in ALLOWED_USERS:
        return
    
    await update.message.reply_text(random.choice(compliments))

async def memory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random memory"""
    if update.effective_user.id not in ALLOWED_USERS:
        return
    
    await update.message.reply_text(random.choice(memories))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show available commands"""
    if update.effective_user.id not in ALLOWED_USERS:
        return
    
    help_text = """
Available commands:
/start - Start the bot
/compliment - Get a sweet compliment
/memory - Get a cherished memory
/help - Show this help message
    """
    await update.message.reply_text(help_text)

# 🕒 Scheduled Message Functions
async def send_cute_question():
    """Send cute question to all allowed users"""
    global application
    if application is None:
        return
        
    for user_id in ALLOWED_USERS:
        try:
            await application.bot.send_message(
                chat_id=user_id, 
                text="Aap itni cute kyun ho? 🥹"
            )
            await asyncio.sleep(1)
            await application.bot.send_message(
                chat_id=user_id, 
                text="Jatin ko ek daar dena zaroor aaj 😛"
            )
        except Exception as e:
            logger.error(f"Error sending cute question to {user_id}: {e}")

async def send_daily_greetings():
    """Send time-appropriate greetings"""
    global application
    if application is None:
        return
        
    # Simple time handling without timezone complications
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
        try:
            await application.bot.send_message(chat_id=user_id, text=msg)
        except Exception as e:
            logger.error(f"Error sending greeting to {user_id}: {e}")

# 🔄 Background Task for Scheduled Messages
async def scheduled_messages():
    """Background task to send scheduled messages"""
    last_greeting_hour = -1
    cute_question_counter = 0
    
    while True:
        try:
            current_hour = datetime.datetime.now().hour
            
            # Send greetings every 6 hours (at 6, 12, 18, 0)
            if current_hour in [6, 12, 18, 0] and current_hour != last_greeting_hour:
                await send_daily_greetings()
                last_greeting_hour = current_hour
                logger.info(f"Sent daily greeting at hour {current_hour}")
            
            # Send cute questions every 4 hours
            cute_question_counter += 1
            if cute_question_counter >= 240:  # 240 minutes = 4 hours
                await send_cute_question()
                cute_question_counter = 0
                logger.info("Sent cute question")
            
            await asyncio.sleep(60)  # Check every minute
            
        except Exception as e:
            logger.error(f"Error in scheduled messages: {e}")
            await asyncio.sleep(60)

# 🚀 Main Application
async def main():
    """Main function to run the bot"""
    global application
    
    try:
        # Create application with minimal configuration
        application = (
            Application.builder()
            .token(TOKEN)
            .build()
        )
        
        # Add command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("compliment", compliment))
        application.add_handler(CommandHandler("memory", memory))
        application.add_handler(CommandHandler("help", help_command))
        
        # Start background task for scheduled messages
        asyncio.create_task(scheduled_messages())
        
        print("Bot is running now... ✅")
        logger.info("Bot started successfully")
        
        # Run the bot with minimal settings
        await application.run_polling(
            drop_pending_updates=True,
            allowed_updates=Update.ALL_TYPES
        )
        
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped by user")
    except Exception as e:
        print(f"Fatal error: {e}")
        logger.error(f"Fatal error: {e}")
