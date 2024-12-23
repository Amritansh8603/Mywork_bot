from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
from datetime import datetime
import os

# 1. Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your basic Telegram bot. Type /help to see what I can do.')

# 2. Help Command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here are my commands:\n'
                                    '/start - Greet the user\n'
                                    '/help - Show available commands\n'
                                    '/echo <message> - I will repeat your message\n'
                                    '/bye - Say goodbye\n'
                                    '/joke - I will tell you a random joke\n'
                                    '/time - I will tell you the current time')

# 3. Echo Command
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = ' '.join(context.args)
    if user_message:
        await update.message.reply_text(f'You said: {user_message}')
    else:
        await update.message.reply_text('Please provide a message after /echo')

# 4. Bye Command
async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Goodbye! Have a great day!')

# 5. Joke Command
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    jokes = [
        "Why don't programmers like nature? It has too many bugs!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!"
    ]
    await update.message.reply_text(random.choice(jokes))

# 6. Time Command
async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await update.message.reply_text(f'The current time is: {current_time}')

# Main Function
def main():
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    token = '7820522890:AAEERFwrjziuSXOrBo_JNKYBENpTBlhwfMI'

    # Optional: Set up proxy settings if needed
    proxy_url = os.getenv('TELEGRAM_PROXY_URL', '')  # Use environment variable for security
    application = Application.builder().token(token)

    if proxy_url:
        # For example, you can set HTTP proxy like this if needed
        application = application.proxy(proxy_url)

    # Build the application
    application = application.build()

    # Add command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('echo', echo))
    application.add_handler(CommandHandler('bye', bye))
    application.add_handler(CommandHandler('joke', joke))
    application.add_handler(CommandHandler('time', time))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
   