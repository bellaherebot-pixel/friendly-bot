import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import random
from datetime import datetime
import os

TOKEN = "86581915783:AAE-X1UWG6_djR0KNI_D7_CO8b4UF9K0XA10"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

promotions = []
user_points = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    await update.message.reply_text(f"✨ BELLAHEREBOT! Hola {user}! 🦋\n\n/help - Commands dekho")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
🎮 GAMES:
/truth, /dare, /wyr, /nhie

😂 MASTI:
/joke, /fact, /quote, /shayari, /love, /attitude

📢 PROMOTION:
/promote [text], /promotions, /randompromo
    """)

async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    truths = ["Crush ka naam?", "Last time roya?", "Body count?"]
    await update.message.reply_text(f"🎯 TRUTH: {random.choice(truths)}")

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dares = ["Kisi ko I love you bol", "Photo bhej", "10 pushups kar"]
    await update.message.reply_text(f"🔥 DARE: {random.choice(dares)}")

async def wyr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = random.choice([("Ex ke saath trip", "10 lakh cash"), ("Famous hona", "Rich hona")])
    await update.message.reply_text(f"🤔 WYR:\nA) {q[0]}\nB) {q[1]}")

async def nhie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    n = ["Kabhi exam mein copy nahi mari", "Kabhi jhooth nahi bola"]
    await update.message.reply_text(f"🫣 NHIE: {random.choice(n)}")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = ["Santa: Doctor meri yaadash weak hai\nDoctor: Kab se?\nSanta: Kya kab se? 😂"]
    await update.message.reply_text(f"😂 JOKE: {random.choice(jokes)}")

async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    facts = ["🧠 Octopus ke 3 dil hote hain", "🍌 Banana ek berry hai"]
    await update.message.reply_text(f"🧠 FACT: {random.choice(facts)}")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = ["Hard times create strong men 🗿", "Self love is the best love 💕"]
    await update.message.reply_text(f"💫 QUOTE: {random.choice(quotes)}")

async def shayari(update: Update, context: ContextTypes.DEFAULT_TYPE):
    shayaris = ["दिल टूटता है तो आवाज़ नहीं होती 💔"]
    await update.message.reply_text(f"😔 SHAYARI: {random.choice(shayaris)}")

async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❤️ तुम सबको प्यार!")

async def attitude(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("😎 मैं हूँ ना, बाकी लोग side में!")

async def promote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("/promote [text] likho")
        return
    text = ' '.join(context.args)
    promotions.append({'text': text, 'user': update.effective_user.first_name})
    await update.message.reply_text(f"✅ Promotion add: {text}")

async def view_promotions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not promotions:
        await update.message.reply_text("Koi promotion nahi")
        return
    msg = "📢 Promotions:\n"
    for p in promotions[-5:]:
        msg += f"• {p['text']} (by {p['user']})\n"
    await update.message.reply_text(msg)

async def random_promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not promotions:
        await update.message.reply_text("Koi promotion nahi")
        return
    p = random.choice(promotions)
    await update.message.reply_text(f"🎲 Random: {p['text']} (by {p['user']})")

async def bella(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✨ Main hoon Bella! Group ki virtual bestie!")
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("truth", truth))
    app.add_handler(CommandHandler("dare", dare))
    app.add_handler(CommandHandler("wyr", wyr))
    app.add_handler(CommandHandler("nhie", nhie))
    app.add_handler(CommandHandler("joke", joke))
    app.add_handler(CommandHandler("fact", fact))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("shayari", shayari))
    app.add_handler(CommandHandler("love", love))
    app.add_handler(CommandHandler("attitude", attitude))
    app.add_handler(CommandHandler("promote", promote))
    app.add_handler(CommandHandler("promotions", view_promotions))
    app.add_handler(CommandHandler("randompromo", random_promo))
    app.add_handler(CommandHandler("bella", bella))
    print("🚀 BELLAHEREBOT CHAL RAHA!")
    app.run_polling()

if name == "main":

    main()
