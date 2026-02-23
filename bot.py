import logging
import os
import random

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Token direct code mein daal diya
TOKEN = "8658191578:AAE-X1uM6_djRokn_D7_COm6u4F9K0XA10"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Promotions store karne ke liye list
promotions = []

# ==================== START COMMAND ====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    await update.message.reply_text(f"Hello {user}! 🤗 Main hoon Bella! \n/help se commands dekho.")

# ==================== HELP COMMAND ====================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
📚 COMMANDS:
/truth - Sach bol
/dare - Kar dikha
/promote [text] - Promotion daalo
/promotions - Sab promotions dekho
    """)

# ==================== TRUTH COMMAND ====================
async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    truths = [
        "Crush ka naam bata? 😳",
        "Last time kab roya tha? 😭",
        "Body count kitna hai? 💀",
        "Kabhi kiss kiya hai? 💋",
        "Group mein kispe crush hai? 🤭"
    ]
    await update.message.reply_text(f"🎯 TRUTH: {random.choice(truths)}")

# ==================== DARE COMMAND ====================
async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dares = [
        "Kisi ko I love you bol ke dikha 📞",
        "Apni photo bhej group mein 📸",
        "10 pushups kar ke video bhej 💪",
        "Ex ko text kar 'Miss you' 💌",
        "Voice note mein gaana ga 🎤"
    ]
    await update.message.reply_text(f"🔥 DARE: {random.choice(dares)}")

# ==================== PROMOTE COMMAND ====================
async def promote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Kya promote karwana hai? /promote [text] likh")
        return
    
    text = ' '.join(context.args)
    user = update.effective_user.first_name
    promotions.append({'user': user, 'text': text})
    await update.message.reply_text(f"✅ Promotion added: {text}")

# ==================== VIEW PROMOTIONS ====================
async def view_promotions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not promotions:
        await update.message.reply_text("Koi promotion nahi hai!")
        return
    
    msg = "📢 Promotions:\n"
    for p in promotions[-5:]:
        msg += f"• {p['text']} (by {p['user']})\n"
    await update.message.reply_text(msg)

# ==================== MAIN FUNCTION ====================
def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("truth", truth))
    app.add_handler(CommandHandler("dare", dare))
    app.add_handler(CommandHandler("promote", promote))
    app.add_handler(CommandHandler("promotions", view_promotions))
    
    print("🚀 BELLA BOT CHAL RAHA HAI!")
    app.run_polling()

if __name__ == "__main__":
    main()
